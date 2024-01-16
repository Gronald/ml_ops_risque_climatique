from src.main import get_prediction
from src.main import app
import json
from fastapi.testclient import TestClient


client = TestClient(app)



# https://fastapi.tiangolo.com/tutorial/testing/

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "MC Intro MLOPS"}


# def test_predict_endpoint():
#     # Test avec des valeurs valides
#     data = {
#         "latitude": 40.0,
#         "longitude": -75.0,
#         "annee": 2022
#     }
#     response = client.post("/predict", json=data)
#     assert response.status_code == 200
#     assert "prediction" in response.json()
#     assert "probability" in response.json()

# def test_predict_endpoint_invalid_input():
#     # Test avec des valeurs invalides
#     data = {
#         "latitude": 100.0, 
#         "longitude": -75.0,
#         "annee": 2022
#     }
#     response = client.post("/predict", json=data)
#     assert response.status_code == 422  # Erreur de validation des données

# def test_predict_endpoint_invalid_credentials():
#     # Test avec des informations d'authentification incorrectes
#     data = {
#         "latitude": 40.0,
#         "longitude": -75.0,
#         "annee": 2022
#     }
#     response = client.post("/predict", json=data, headers={"Authorization": "Basic invalid_credentials"})
#     assert response.status_code == 401  # Invalid credentials

# def test_view_logs_endpoint():
#     # Test de l'endpoint view-logs pour un utilisateur admin
#     response = client.get("/view-logs", headers={"Authorization": "Basic dXNlcjE6cGFzc3dvcmQx"}) 
#     assert response.status_code == 200
#     assert "logs" in response.json()

# def test_view_logs_endpoint_non_admin():
#     # Test de l'endpoint view-logs pour un utilisateur non admin
#     response = client.get("/view-logs", headers={"Authorization": "Basic dXNlcjI6cGFzc3dvcmQy"})  # Remplacez les informations d'authentification
#     assert response.status_code == 403  # Permission denied


def tests_unitaires():
    
    """rentrer une valeur et voir sa vaeur attendue"""
    assert(get_prediction(46.15373399404384, 4.925852382365117, 1984).get('prediction')) == 0
    #Trouver un exemple avec un 1 ou refaire le modele avec k = 1
    
    #Test sur l'annee
    assert(get_prediction(46.15373399404384, 4.925852382365117, 2024)) == "Erreur dans la saisie"

    #Test sur la latitude
    assert(get_prediction(-100, 4.925852382365117, 1984)) == "Erreur dans la saisie"

     #Test sur la longitude
    assert(get_prediction(46.15373399404384, -100, 1984)) == "Erreur dans la saisie"

    