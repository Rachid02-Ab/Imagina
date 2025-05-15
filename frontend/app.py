import streamlit as st
import requests
import json
import random

st.set_page_config(
    page_title="Imagina - L'Art de l'Imagination",
    page_icon="🎭",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #fafafa;
    }
    .main-title {
        background: linear-gradient(45deg, #2E3192, #1BFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5em !important;
        text-align: center;
        padding: 20px;
        font-weight: 300;
        letter-spacing: 2px;
    }
    .assistant-message {
        background: linear-gradient(to right, #f8f9fa, #ffffff);
        padding: 25px;
        border-radius: 12px;
        margin: 20px 0;
        border: 1px solid #eaecef;
        font-style: italic;
        color: #4a4a4a;
    }
    .stButton button {
        background: linear-gradient(45deg, #2E3192, #1BFFFF);
        border: none;
        color: white;
        font-weight: 400;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>Imagina</h1>", unsafe_allow_html=True)

# Messages d'accueil élégants
welcome_messages = [
    "Transformez vos pensées en images...",
    "Où l'imagination prend forme",
    "Créez l'extraordinaire",
    "Donnez vie à vos idées",
]

st.markdown(f"<div class='assistant-message'>{random.choice(welcome_messages)}</div>", unsafe_allow_html=True)

# Suggestions de prompts
example_prompts = [
    "une bibliothèque infinie aux escaliers impossibles",
    "un jardin japonais sous la pluie d'automne",
    "une ville art déco baignée de lumière dorée",
    "un café parisien au petit matin",
]

# Sidebar configuration
with st.sidebar:
    st.header("🎨 Création")
    
    # Prompt section
    st.subheader("Vision")
    if st.button("Inspiration"):
        prompt = st.text_area("Description", value=random.choice(example_prompts), height=100)
    else:
        prompt = st.text_area("Description", 
                            placeholder="Décrivez votre vision...",
                            height=100)
    
    # Style section
    st.subheader("Format")
    image_size = st.selectbox(
        "Proportions",
        ["landscape_4_3", "portrait_3_4", "square_1_1"],
        format_func=lambda x: {
            "landscape_4_3": "Paysage (4:3)",
            "portrait_3_4": "Portrait (3:4)",
            "square_1_1": "Carré (1:1)"
        }[x]
    )
    
    # Advanced options
    with st.expander("Paramètres"):
        seed = st.number_input("Seed", value=random.randint(1, 1000000), help="Pour reproduire une création")
        num_images = st.slider("Variations", min_value=1, max_value=4, value=1)

# Main content
if st.button("Créer", type="primary", use_container_width=True):
    if not prompt:
        st.error("Partagez votre vision pour commencer...")
    else:
        with st.spinner("Création en cours..."):
            try:
                response = requests.post(
                    "http://localhost:8000/generate-image",
                    json={
                        "prompt": prompt,
                        "seed": seed,
                        "image_size": image_size,
                        "num_images": num_images
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    st.markdown("### Créations")
                    
                    # Create columns based on number of images
                    cols = st.columns(num_images)
                    
                    # Display images in columns
                    for idx, image_data in enumerate(result["result"]):
                        with cols[idx]:
                            st.image(image_data["image"], caption=f"Variation {idx+1}")
                            st.download_button(
                                "Télécharger",
                                data=image_data["image"],
                                file_name=f"imagina_{idx+1}.png",
                                mime="image/png"
                            )
                else:
                    st.error("Une erreur est survenue. Veuillez réessayer.")
                    
            except Exception as e:
                st.error(f"Erreur : {str(e)}")

# Tips section
with st.expander("Conseils"):
    st.markdown("""
    - Soyez précis dans vos descriptions
    - Ajoutez des détails sur l'ambiance
    - Expérimentez avec différents styles
    - Notez les seeds de vos créations préférées
    """)

# Footer
st.markdown("---")
st.markdown("Imagina - L'art de donner vie à vos idées") 