from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials 
from pydantic import BaseModel, Field, validator 
import json 
from datetime import datetime
import os 
json_file_path = "results_query.json"

from joblib import load 

clf = load('./models/model.joblib')



# Configurer l'authentification HTTP Basic 
security = HTTPBasic()

# Définir une liste d'utilisateurs avec des noms d'utilisateur, des mots de passe et des rôles 
users_db = [
    {"username": "user1", "password": "password1", "role": "admin"},
    {"username": "user2", "password": "password2", "role": "regular_user"} ]

# A mettre dans predict_model


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
        if not 1982 <= value <= 2023:
            raise ValueError(f"L'année doit être comprise entre 1982 et 2023.")
        return value

def test_inputs(latitude,longitude,annee) :

    if not 1982 <= annee <= 2023:
         annee =  None
    if  not  -90 <= latitude  <= 90 :
        latitude = None
    if not -90 <= longitude <= 90 : 
        longitude = None

    return latitude, longitude, annee


def get_prediction(latitude, longitude, annee):
    
    if not None in test_inputs(latitude,longitude,annee) : 

        x = [[latitude, longitude, annee]]

        prediction = clf.predict(x)[0]
        probability = clf.predict_proba(x).max()

        results = {"prediction": int(prediction), "probability": float(probability)}
    else :
        results = "Erreur dans la saisie"

    return results

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


@app.post("/predict")
def predict(params : ModelParams,user: dict = Depends(get_current_user)):
    pred = get_prediction(params.latitude, params.longitude, params.annee)

    log_info = {
        'datetime': datetime.utcnow().isoformat(),
        'user': user["username"],
        'latitude': params.latitude,
        'longitude': params.longitude,
        'annee': params.annee,
        'prediction': pred.get('prediction'),
        'probability': pred.get('probability')
    }

    with open(os.path.join("data","logs",json_file_path), 'r') as log_file:
        existing_data = json.load(log_file)

    existing_data.append(log_info)

    #Stockage des logs dans un fichier JSON
    with open(os.path.join("data","logs",json_file_path), 'w') as updated_file:
        json.dump(existing_data,updated_file)

    return pred


@app.get("/")
async def read_main():
    return {"msg": "MC Intro MLOPS"}

#Endpoint pour afficher les logs si l'utilisateur est un administrateur
@app.get("/view-logs")
def view_logs(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Permission denied. Admin access required.")

    # Lire le fichier JSON et renvoyer son contenu
    with open(os.path.join("data","logs",json_file_path), 'r') as log_file:
        logs_content = json.load(log_file)

    return logs_content
