Waire

**Waire** est un projet mobile de reconnaissance de connecteurs et de câbles à partir de photos, basé sur l'intelligence artificielle.

## Objectif

Développer une application capable de :
- Identifier automatiquement des connecteurs à partir de photos (ex : USB-C, HDMI, DisplayPort...).
- Proposer une fiche descriptive pour chaque connecteur reconnu.
- À terme, recommander des câbles compatibles entre différents appareils (PC, écrans, etc.).

## Architecture du projet

Waire/ 
│ 
├── dev/ # Application mobile en React Native 
├── dataset/ # Images collectées pour entraîner l'IA 
├── scraper/ # Scripts de scraping Selenium + traitement d'images avec PIL 
├── AI/ # Modèles IA, notebooks d'entraînement, expérimentations 
└── README.md # Documentation du projet


## Technologies utilisées

- **React Native** : pour développer l'application mobile.
- **Python** : pour les scripts de scraping et le traitement d'images.
- **Selenium** : pour la collecte automatisée d'images sur Internet.
- **Pillow (PIL)** : pour redimensionner, convertir et améliorer les images.
- **TensorFlow / Keras** (ou autre framework IA) : pour créer et entraîner le modèle de reconnaissance.

## État d'avancement

- [x] Définition de l'idée principale
- [x] Mise en place du script de collecte d'images
- [ ] Constitution d'un dataset initial d'images
- [ ] Développement de l'application mobile de base
- [ ] Entraînement et évaluation du premier modèle IA
- [ ] Déploiement de l'application sur Android (Play Store)

## Installation et lancement

> Ce projet est actuellement en cours de développement.
> Les instructions détaillées d'installation viendront prochainement.

## Roadmap prévisionnelle

- Créer un premier dataset structuré avec suffisamment d'images (500 à 1000 par connecteur).
- Prototyper un modèle de classification IA simple.
- Développer une première version mobile "reconnaissance seule".
- Ajouter progressivement :
  - Suggestions de câbles compatibles
  - Fiches détaillées pour chaque connecteur
  - Vérification de compatibilité entre appareils

## À venir

- Système serveur léger pour la gestion des modèles IA.
- Amélioration continue de la base de données de connecteurs.
- Version iOS de l'application (long terme).

---

> Projet initié par **[Nathan Lemonnier]** – 2025.