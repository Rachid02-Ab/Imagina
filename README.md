# Imagina - L'Art de l'Imagination

Imagina est une application web élégante qui transforme vos descriptions textuelles en œuvres d'art grâce à l'intelligence artificielle. Une interface épurée et intuitive qui donne vie à vos idées.

## ✨ Caractéristiques

- Interface minimaliste et élégante
- Génération d'images basée sur du texte
- Formats multiples (Paysage, Portrait, Carré)
- Suggestions créatives intégrées
- Expérience utilisateur fluide et intuitive

## 🛠️ Technologies

- Frontend: Streamlit
- Backend: FastAPI
- IA: fal.ai
- CI/CD: GitHub Actions

## 📦 Installation

1. Clonez le repository :
```bash
git clone <votre-repo>
cd imagina
```

2. Créez un fichier `.env` à la racine du projet :
```
FAL_KEY=votre_clé_api
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## 🚀 Démarrage

1. Lancez le backend :
```bash
cd backend
python -m uvicorn main:app --reload
```

2. Lancez l'interface :
```bash
cd frontend
python -m streamlit run app.py
```

## 🌐 Déploiement

L'application se déploie automatiquement sur Streamlit Cloud à chaque push sur la branche main.

### Configuration

1. Créez un compte sur [Streamlit Cloud](https://streamlit.io/cloud)

2. Configurez les secrets GitHub :
   - `STREAMLIT_CREDENTIALS` : Identifiants Streamlit Cloud
   - `FAL_KEY` : Clé API fal.ai

3. Le déploiement s'effectue automatiquement via GitHub Actions

## 💡 Guide d'utilisation

1. Accédez à l'application :
   - En production : via l'URL Streamlit Cloud
   - En local : `http://localhost:8501`
2. Décrivez l'image souhaitée
3. Personnalisez les paramètres
4. Cliquez sur "Créer"

## 🤝 Contribution

Les contributions sont bienvenues :
1. Forkez le projet
2. Créez une branche (`git checkout -b feature/NouvelleFonctionnalité`)
3. Commitez vos changements (`git commit -m 'Ajout de NouvelleFonctionnalité'`)
4. Pushez vers la branche (`git push origin feature/NouvelleFonctionnalité`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

*Imagina - Où l'imagination prend forme* 