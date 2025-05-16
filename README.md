# Imagina - L'Art de l'Imagination

<div align="center">
  <img src="demo/Imagina.gif" alt="Démonstration Imagina" width="800"/>
</div>

Imagina est une application élégante qui transforme vos descriptions textuelles en œuvres d'art grâce à un modèle de diffusion stable **FLUX.1-dev**. il prend vos prompts et les tranforment en art visuel. Une interface épurée et intuitive qui donne vie à vos idées.

## 🛠️ Stack Technique

### FLUX.1-dev Model by HuggingFace:
- **Modèle**: [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) par Black Forest Labs
  - Architecture: 
    - Transformeur à flux rectifié de 12 milliards de paramètres
    - Blocs de transformeur de diffusion multimodaux et parallèles
    - Optimisé par distillation de guidage pour l'efficacité
  - Capacités Techniques:
    - Génération haute résolution (1024x768)
    - Support multi-formats (paysage, portrait, carré)
    - Contrôle précis via seed pour la reproductibilité
    - Optimisé pour la qualité visuelle
    - Traitement de contexte jusqu'à 512 tokens
    - Support de génération de 0.1 à 2 mégapixels
  - Pipeline de Génération:
    - Encodage du texte en représentation latente
    - Processus de diffusion guidée
    - Décodage via auto-encodeur optimisé
    - Post-traitement pour amélioration de la qualité



### Frontend (Streamlit):
- **Framework**: Streamlit
  - Interface réactive et moderne
  - Composants personnalisés pour l'expérience utilisateur
  - Gestion d'état efficace
  - Prévisualisation en temps réel
  - Support de téléchargement d'images
  - Thème personnalisé et responsive

### DevOps:
- **CI Pipeline** via GitHub Actions:
  - Linting avec flake8:
    - Vérification des erreurs critiques (E9, F63, F7, F82)
    - Analyse de la complexité du code (max-complexity=10)
    - Vérification de la longueur des lignes (max-line-length=127)
  - Formatage automatique avec black
  - Tests automatisés
  - Déclencheurs:
    - Push sur main
    - Pull requests
    - Déclenchement manuel (workflow_dispatch)

### Sécurité et Performance:
- Gestion sécurisée des clés API
- Rate limiting pour protection API
- Optimisation des ressources GPU
- Mise en cache intelligente des résultats
- Monitoring des performances
- Logs structurés pour le debugging





