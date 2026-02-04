import os
from fastapi.testclient import TestClient
from app.main import app # Vérifie que le nom du fichier est bien main.py

client = TestClient(app)

def test_health_check():
    """Vérifie que l'API est en ligne"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_debug_endpoint_security():
    """Vérifie que l'endpoint debug renvoie bien des variables d'environnement"""
    # On définit une variable temporaire pour le test
    os.environ["TEST_VAR"] = "secret_value"

    response = client.get("/debug")
    assert response.status_code == 200
    data = response.json()

    # On vérifie que notre variable est présente dans la réponse
    assert "env" in data
    assert data["env"]["TEST_VAR"] == "secret_value"
