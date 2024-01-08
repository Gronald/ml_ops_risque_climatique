from fastapi import FastAPI, Depends, HTTPException 
from fastapi.security import HTTPBasic, HTTPBasicCredentials 
from joblib import load 
from pydantic import BaseModel, Field, validator 
import json 
from datetime import datetime

# Configurer le système de logs
import logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Configurer l'authentification HTTP Basic 

security = HTTPBasic()

# Définir une liste d'utilisateurs avec des noms d'utilisateur, des mots de passe et des rôles 
users_db = [
    {"username": "user1", "password": "password1", "role": "admin"},
    {"username": "user2", "password": "password2", "role": "regular_user"} ]

# A mettre dans predict_model
clf = load('models/model.joblib')

class ModelParams(BaseModel):
    latitude: float = Field(..., description="La latitude doit être un nombre décimal.")
    longitude: float = Field(..., description="La longitude doit être un nombre décimal.")
    annee: int = Field(..., description="L'année doit être un nombre entier.")

    @validator("latitude", "longitude")
    def validate_coordinates(cls, value):
        if not -90 <= value <= 90:
            raise ValueError("Les coordonnées doivent être comprises entre -90 et 90.")
        return value

    @validator("annee")
    def validate_year(cls, value):
        current_year = datetime.now().year
        if not 1900 <= value <= current_year:
            raise ValueError(f"L'année doit être comprise entre 1900 et {current_year}.")
        return value

def get_prediction(latitude, longitude, annee):
    # Tests sur les paramètres

    x = [[latitude, longitude, annee]]

    prediction = clf.predict(x)[0]
    probability = clf.predict_proba(x).max()

    # Construire un dictionnaire avec les informations
    log_info = {
        #Rajouter user
        'datetime': datetime.utcnow().isoformat(),
        'latitude': latitude,
        'longitude': longitude,
        'annee': annee,
        'prediction': prediction,
        'probability': probability
    }

    # Stocker les logs dans un fichier JSON
    with open('logs/app_logs.json', 'a') as log_file:
        log_file.write(json.dumps(log_info) + '\n')

    return {'prediction': prediction, 'probability': probability} # Fin 

# Initier l'API
app = FastAPI()

# Définir l'authentification HTTP Basic
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = authenticate_user(credentials.username, credentials.password)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

def authenticate_user(username: str, password: str):
    # Rechercher l'utilisateur dans la liste d'utilisateurs
    for user in users_db:
        if user["username"] == username and user["password"] == password:
            return {"username": user["username"], "role": user["role"]}
    return None

# Exemple d'utilisation de l'authentification dans la route
@app.post("/predict")
def predict(params: ModelParams, user: dict = Depends(get_current_user)):
    # Vérifier le rôle de l'utilisateur 
    # check users

    pred = get_prediction(params.latitude, params.longitude, params.annee)
    return pred

# Nouvelle route pour afficher le JSON si l'utilisateur est un administrateur
@app.get("/view-logs")
def view_logs(user: dict = Depends(get_current_user)):
    # Vérifier le rôle de l'utilisateur
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Permission denied. Admin access required.")

    # Lire le fichier JSON et renvoyer son contenu
    with open('logs/app_logs.json', 'r') as log_file:
        logs_content = log_file.readlines()

    return {"logs": logs_content}
