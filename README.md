# Compteur de visites — Flask + Redis + Docker + CI/CD

Projet DevOps démontrant la conteneurisation d'une app web et l'automatisation
via un pipeline CI/CD GitHub Actions.

## Stack technique

| Composant | Technologie |
|-----------|-------------|
| Application | Python Flask |
| Base de données | Redis 7 |
| Conteneurisation | Docker + Docker Compose |
| Pipeline CI/CD | GitHub Actions |

## Architecture

```
Navigateur → http://localhost:5001
                    ↓
            [Container: flask_app]
             Flask app (port 5000)
                    ↓ redis:6379
            [Container: redis_db]
             Redis (volume persistant)
```

## Pipeline CI/CD

```
git push → GitHub → GitHub Actions
                          ↓
                   1. Build image Docker
                          ↓
                   2. Start docker-compose
                          ↓
                   3. Test HTTP (curl → 200 OK)
                          ↓
                   4. docker-compose down
```

## Lancer le projet en local

### Prérequis
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé

### Démarrage

```bash
# 1. Cloner le projet
git clone https://github.com/TON_USERNAME/visit-counter.git
cd visit-counter

# 2. Lancer les containers
docker-compose up -d --build

# 3. Ouvrir dans le navigateur
http://localhost:5001
```

### Commandes utiles

```bash
docker ps                  # Voir les containers
docker logs flask_app      # Logs de l'app
docker-compose down        # Arrêter
docker-compose down -v     # Arrêter + supprimer volumes
```

## Structure du projet

```
visit-counter/
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline GitHub Actions
├── app/
│   ├── app.py              # Application Flask
│   ├── requirements.txt    # Dépendances Python
│   ├── Dockerfile          # Image Docker de l'app
│   └── templates/
│       └── index.html      # Page web
├── docker-compose.yml      # Orchestration des services
└── README.md
```

## Ce que ce projet démontre

- Dockerfile optimisé (cache des layers)
- Orchestration multi-conteneurs avec docker-compose
- Communication inter-containers via réseau Docker
- Persistance des données avec volume Docker
- Pipeline CI/CD automatisé avec GitHub Actions
- Test HTTP automatique à chaque git push
