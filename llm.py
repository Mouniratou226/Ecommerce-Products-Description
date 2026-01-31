# llm.py - VERSION SIMPLIFIÉE ET ROBUSTE
import os
import traceback
from google import genai

def generate_description(prompt):
    """
    Envoie le prompt à l'API Gemini et retourne la réponse texte.
    """
    try:
        # Récupérer la clé DANS la fonction (plus fiable)
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            raise ValueError(" GOOGLE_API_KEY non trouvée. Vérifiez le chargement de .env dans main.py")
        
        # Initialiser le client avec la clé
        client = genai.Client(api_key=api_key)
        
        # Appel API simple
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text
        
    except Exception as e:
        print(f"\n{'='*60}")
        print("❌ ERREUR DANS generate_description:")
        print(f"Message: {e}")
        traceback.print_exc()
        print(f"{'='*60}\n")
        raise e