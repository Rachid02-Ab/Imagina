from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import fal_client
import os
from dotenv import load_dotenv
from typing import List, Optional, Dict
import time

# Load environment variables
load_dotenv()

# Vérifier la présence de la clé API
if not os.getenv("FAL_KEY"):
    raise EnvironmentError("La clé API FAL_KEY n'est pas définie dans le fichier .env")

app = FastAPI(
    title="ArtBot API",
    description="API pour ArtBot - Votre assistant de création d'images IA",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageRequest(BaseModel):
    prompt: str = Field(..., description="Description de l'image à générer")
    seed: int = Field(default=42, description="Seed pour la reproduction des résultats")
    image_size: str = Field(
        default="landscape_4_3",
        description="Format de l'image",
        enum=["landscape_4_3", "portrait_3_4", "square_1_1"]
    )
    num_images: int = Field(
        default=1,
        ge=1,
        le=4,
        description="Nombre d'images à générer (1-4)"
    )

class ImageData(BaseModel):
    url: str
    width: int
    height: int
    content_type: str

class GenerationResponse(BaseModel):
    status: str
    result: List[Dict]
    generation_time: float
    prompt: str

@app.post("/generate-image", response_model=GenerationResponse)
async def generate_image(request: ImageRequest):
    try:
        start_time = time.time()
        
        # Amélioration du prompt pour de meilleurs résultats
        enhanced_prompt = f"{request.prompt}, high quality, detailed, professional"
        
        result = fal_client.subscribe(
            "fal-ai/flux/dev",
            arguments={
                "prompt": enhanced_prompt,
                "seed": request.seed,
                "image_size": request.image_size,
                "num_images": request.num_images
            },
        )

        # Transformer la réponse en format attendu
        transformed_result = []
        if isinstance(result, dict) and 'images' in result:
            for image in result['images']:
                transformed_result.append({
                    'image': image['url'],
                    'width': image.get('width', 0),
                    'height': image.get('height', 0),
                    'content_type': image.get('content_type', 'image/jpeg')
                })
        
        generation_time = time.time() - start_time
        
        return {
            "status": "success",
            "result": transformed_result,
            "generation_time": round(generation_time, 2),
            "prompt": enhanced_prompt
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Erreur lors de la génération de l'image",
                "error": str(e)
            }
        )

@app.get("/health")
async def health_check():
    """Vérifie l'état de santé de l'API"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "service": "ArtBot API"
    } 