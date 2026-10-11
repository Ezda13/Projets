import time
import requests

URL = "https://ku.wikipedia.org/w/api.php"
EN_TETES = {"User-Agent": "corpus-kurmanci/1.0 (projet étudiant ; https://github.com/Ezda13/Projets)"}
NB_ARTICLES = 50
MOTS_MINIMUM = 100


def article_aleatoire():
    parametres = {
        "action": "query",
        "format": "json",
        "generator": "random",
        "grnnamespace": 0,
        "prop": "extracts",
        "explaintext": 1,
    }
    reponse = requests.get(URL, params=parametres, headers=EN_TETES, timeout=30)
    reponse.raise_for_status()
    pages = reponse.json()["query"]["pages"]
    page = list(pages.values())[0]
    return page["title"], page.get("extract", "")


compteur = 0
while compteur < NB_ARTICLES:
    titre, texte = article_aleatoire()
    nb_mots = len(texte.split())
    if nb_mots < MOTS_MINIMUM:
        print("Trop court, ignoré :", titre)
    else:
        compteur += 1
        nom_fichier = f"donnees/article_{compteur:03}.txt"
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            fichier.write(titre + "\n\n" + texte)
        print(compteur, titre, nb_mots, "mots")
    time.sleep(1)