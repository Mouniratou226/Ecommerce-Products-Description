# prompt.py

def build_prompt(product_input):
    """
    Construit un prompt marketing structuré à partir des données du produit.
    """
    prompt_template = f"""
**Prompt unique pour descriptions produits e-commerce premium :**
Tu es un expert en copywriting e-commerce et marketing de conversion. Pour le produit suivant, génère une description complète de haute qualité.

**INFORMATIONS DU PRODUIT :**
- **Nom :** {product_input.product_name}
- **Catégorie :** {product_input.category}
- **Caractéristiques :** {product_input.features}
- **Public cible :** {product_input.target}
- **Avantages uniques :** {product_input.unique_benefits}
- **Prix :** {product_input.price}
- **Ton souhaité :** {product_input.tone}

**STRUCTURE À SUIVRE :**
Commence par un **Titre optimisé SEO** (Marque + Produit + Attribut clé + Mot-clé). Enchaîne avec une **Accroche persuasive** (1-2 phrases sur le bénéfice émotionnel ou la solution). Développe en **3 paragraphes max** : 1) Scénario d'usage quotidien, 2) Transformation/expérience utilisateur, 3) Justification qualité-prix.

Ajoute une **liste à puces techniques & bénéfices** (5-7 points max, format : ✓ [Bénéfice] grâce à [caractéristique]). Puis une section **"Pourquoi nous choisir ?"** avec 3 raisons uniques (fabrication, matériaux, service) et éléments de confiance (garantie, certifications). Termine par un **Appel à l'action fort** avec urgence/scarcité si pertinent (ex: stock limité, offre spéciale).

**CONSIGNES DE STYLE :**
- Adapte le **ton** à la demande : {product_input.tone}.
- Utilise des **mots de pouvoir** (Exclusif, Garanti, Vérifié).
- Intègre naturellement 2-3 **mots-clés SEO** en lien avec le produit.
- Privilégie des **phrases courtes** (<20 mots).
- Utilise un **formatage lisible** (espaces, sauts de ligne, emojis stratégiques : ✓ ★ ✨).

Fournis **uniquement** la description finale, sans commentaires ni texte d'introduction.
"""

    return prompt_template