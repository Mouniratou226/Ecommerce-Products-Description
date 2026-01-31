# main.py - VERSION CORRIGÉE ET TESTÉE
import os
from pathlib import Path
from dotenv import load_dotenv

# 1. CHARGER .env AVANT TOUTE CHOSE
# Chemin absolu vers le fichier .env
env_path = Path(__file__).parent / ".env"
print(f"📍 Chargement du fichier .env depuis : {env_path}")

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    print("✅ Fichier .env chargé avec succès")
    
    # DEBUG: Affiche les 10 premiers caractères de la clé
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        print(f"🔑 Clé API détectée (début) : {api_key[:10]}...")
    else:
        print("❌ ERREUR: GOOGLE_API_KEY non trouvée dans .env")
else:
    print(f"❌ ERREUR: Fichier .env introuvable à {env_path}")

# 2. IMPORTER LES AUTRES MODULES (APRÈS avoir chargé .env)
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from models import ProductInput
from prompt import build_prompt
from llm import generate_description

# 3. CRÉER L'APPLICATION
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
def generate(product: ProductInput = Body(...)):
    prompt = build_prompt(product)
    result = generate_description(prompt)
    return {"content": result}