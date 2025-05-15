# Imagina - L'Art de l'Imagination

<div align="center">
  <img src="demo/Imagina.gif" alt="Démonstration Imagina" width="800"/>
</div>

Imagina est une application web élégante qui transforme vos descriptions textuelles en œuvres d'art grâce à un modele de diffusion stable. Une interface épurée et intuitive qui donne vie à vos idées.

## 🛠️ Stack Technique
### FLUX.1-dev Model by HuggingFace:
- **Modèle**: [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) par Black Forest Labs
  - Architecture: Diffusion stable optimisée
  - Capacités:
    - Génération haute résolution (1024x768)
    - Support multi-formats (paysage, portrait, carré)
    - Contrôle précis via seed
    - Optimisé pour la qualité visuelle


### Backend
- **Framework**: FastAPI
  - ASGI server: Uvicorn
  - Validation des données: Pydantic v2
  - CORS middleware
  - Gestion asynchrone des requêtes

### Frontend
- **Framework**: Streamlit
  - Interface réactive
  - Composants personnalisés
  - Gestion d'état

### DevOps
- **CI/CD**: GitHub Actions
  - Linting: flake8
  - Formatage: black
  - Tests automatisés
  - Vérification de la qualité du code





