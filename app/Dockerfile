# Image de base légère Python
FROM python:3.11-slim

# Répertoire de travail dans le container
WORKDIR /app

# Copier et installer les dépendances d'abord (optimise le cache Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port utilisé par Flask
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]
