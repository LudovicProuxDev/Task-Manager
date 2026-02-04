# 1. Utilise une version stable et spécifique
FROM python:3.11-slim-bookworm

# 2. Empêche Python de générer des fichiers .pyc et d'utiliser un buffer pour les logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 3. Optimisation du cache : on installe les dépendances d'abord
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copie le reste du code (en supposant que tu es dans le dossier backend)
COPY backend/ /app/

# 5. Sécurité : Création d'un utilisateur non-privilégié
RUN adduser --disabled-password --gecos "" appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
