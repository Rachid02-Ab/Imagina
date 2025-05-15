# Imagina - L'Art de l'Imagination

<div align="center">
  <img src="demo/Imagina.gif" alt="Démonstration Imagina" width="800"/>
</div>

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
- CI: GitHub Actions (linting et formatage)

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

## 💡 Guide d'utilisation

1. Accédez à l'application en local : `http://localhost:8501`
2. Décrivez l'image souhaitée
3. Personnalisez les paramètres
4. Cliquez sur "Créer"

## 🔍 Qualité du Code

Le projet utilise GitHub Actions pour maintenir la qualité du code :
- Vérification de la syntaxe avec flake8
- Formatage du code avec black
- Tests automatiques à chaque push

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