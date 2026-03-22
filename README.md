# 🔢 Compteur de visites

![CI](https://github.com/YOSO98/visit-counter/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)

Projet DevOps — application web containerisée avec pipeline CI/CD automatisé.

Chaque visite sur la page incrémente un compteur stocké dans Redis.
Les données sont persistées dans un volume Docker, même après redémarrage.

---

## Stack technique

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| Application | Python Flask | Serveur web |
| Base de données | Redis 7 | Stockage du compteur |
| Conteneurisation | Docker + Docker Compose | Orchestration |
| CI/CD | GitHub Actions | Build & Test automatisés |

---

## Architecture

```
Navigateur → http://localhost:5001
                    │
                    ▼
        ┌─────────────────────┐
        │   flask_app         │
        │   Python Flask      │
        │   port 5001 → 5000  │
        └─────────┬───────────┘
                  │ redis:6379
                  ▼
        ┌─────────────────────┐
        │   redis_db          │
        │   Redis 7-alpine    │
        │   volume: db_data   │
        └─────────────────────┘
```

---

## Pipeline CI/CD

```
git push
    │
    ▼
GitHub Actions (ubuntu-latest)
    │
    ├── 1. Checkout code
    ├── 2. Build image Docker
    ├── 3. docker compose up -d
    ├── 4. curl http://localhost:5001 → 200 OK ✅
    ├── 5. docker logs flask_app
    └── 6. docker compose down
```

---

## Lancer le projet en local

### Prérequis
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé et démarré

### Démarrage en une commande

```bash
git clone https://github.com/YOSO98/visit-counter.git
cd visit-counter
docker compose up -d --build
```

Ouvre **http://localhost:5001** dans ton navigateur.

### Commandes utiles

```bash
# Voir les containers qui tournent
docker ps

# Voir les logs de l'app Flask
docker logs flask_app

# Arrêter les containers
docker compose down

# Arrêter et effacer les données Redis
docker compose down -v
```

---

## Structure du projet

```
visit-counter/
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline GitHub Actions
├── app/
│   ├── app.py              # Application Flask (2 routes)
│   ├── Dockerfile          # Image Python 3.11-slim optimisée
│   ├── requirements.txt    # flask + redis
│   └── templates/
│       └── index.html      # Interface web
├── docker-compose.yml      # Orchestration des services
├── .gitignore
└── README.md
```

---

## Ce que ce projet démontre

- **Dockerfile optimisé** : `COPY requirements.txt` avant `COPY . .` pour exploiter le cache des layers Docker
- **Orchestration multi-conteneurs** : communication entre Flask et Redis via le réseau Docker interne (`redis:6379`)
- **Persistance des données** : volume Docker `db_data` — les données survivent aux redémarrages
- **Variables d'environnement** : configuration découplée du code (`REDIS_HOST`)
- **Pipeline CI/CD** : test HTTP automatique à chaque `git push` sur `main`
- **Debug réel** : résolution d'un conflit de port et migration `docker-compose` → `docker compose`

---

## Auteur

**YOSO98** — [github.com/YOSO98](https://github.com/YOSO98)
