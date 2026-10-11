import os
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt

from tokeniser import lire_corpus, decouper_mots, decouper_phrases

MOTS_OUTILS = set([
    "û", "di", "ji", "de", "bi", "li", "ku", "ya", "jî", "ê", "a",
    "xwe", "e", "an", "bo", "wê", "ew", "tê", "bû", "yên", "ye",
    "yê", "re", "ra", "da", "ve", "ev", "vê", "wî", "pê", "lê", "jê",
    "in", "ne", "her", "hem", "heta", "ser", "ber", "wan", "wekî", "van",
    "piştî", "herî", "gelek", "ên", 
    "kirin", "kir", "dike", "dikin", "kirî", "kiriye", "bikin",
    "hatin", "hat", "dihat", "hatîye", "tê", "tên", "hate", "were",
    "dibe", "dibû", "bû", "be",
    "dest", "yek", "din", "wek", "du", "nav", "hin", "divê",
])

MIN_ARTICLES = 3

def frequence_documentaire():
    compteur_articles = Counter()
    for nom in sorted(os.listdir("propre")):
        with open(os.path.join("propre", nom), encoding="utf-8") as fichier:
            mots_article = set(decouper_mots(fichier.read()))
        compteur_articles.update(mots_article)
    return compteur_articles


def graphique_frequences(liste_mots, titre, nom_fichier):
    tableau = pd.DataFrame(Counter(liste_mots).most_common(), columns=["mot", "frequence"])
    tableau.to_csv("resultats/" + nom_fichier + ".csv", index=False, encoding="utf-8-sig")
    top = tableau.head(20)
    plt.figure(figsize=(10, 5))
    plt.bar(top["mot"], top["frequence"], color="#6B1420")
    plt.title(titre)
    plt.xlabel("Mot")
    plt.ylabel("Nombre d'occurrences")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("resultats/" + nom_fichier + ".png")
    plt.close()
    return tableau


os.makedirs("resultats", exist_ok=True)

corpus = lire_corpus()
mots = decouper_mots(corpus)

nb_articles = frequence_documentaire()

mots_pleins = []
for mot in mots:
    if mot not in MOTS_OUTILS and nb_articles[mot] >= MIN_ARTICLES:
        mots_pleins.append(mot)

graphique_frequences(mots, "Les 20 mots les plus fréquents", "mots_frequents")
tableau = graphique_frequences(mots_pleins, "Les 20 mots pleins les plus fréquents", "mots_pleins")

print(tableau.head(20))


# Fréquence des lettres
lettres = []
for mot in mots:
    for lettre in mot:
        lettres.append(lettre)

tableau_lettres = pd.DataFrame(Counter(lettres).most_common(), columns=["lettre", "frequence"])
total = tableau_lettres["frequence"].sum()
tableau_lettres["pourcentage"] = (tableau_lettres["frequence"] / total * 100).round(2)
tableau_lettres.to_csv("resultats/frequences_lettres.csv", index=False, encoding="utf-8-sig")

couleurs = []
for lettre in tableau_lettres["lettre"]:
    if lettre in "êîûçş":
        couleurs.append("#E8A93B")
    else:
        couleurs.append("#6B1420")

plt.figure(figsize=(12, 5))
plt.bar(tableau_lettres["lettre"], tableau_lettres["pourcentage"], color=couleurs)
plt.title("Fréquence des lettres dans le corpus (en doré : lettres spécifiques au kurde)")
plt.xlabel("Lettre")
plt.ylabel("Pourcentage")
plt.tight_layout()
plt.savefig("resultats/lettres.png")
plt.close()

print(tableau_lettres)


# Longueur des phrases
phrases = decouper_phrases(corpus)
longueurs = []
for phrase in phrases:
    nb_mots = len(decouper_mots(phrase))
    if nb_mots > 0:
        longueurs.append(nb_mots)

serie = pd.Series(longueurs)
print(serie.describe().round(1))

courtes = (serie <= 8).sum()
moyennes = ((serie > 8) & (serie <= 20)).sum()
longues = (serie > 20).sum()
print("Phrases courtes (8 mots ou moins) :", courtes)
print("Phrases moyennes (9 à 20 mots) :", moyennes)
print("Phrases longues (plus de 20 mots) :", longues)

plt.figure(figsize=(10, 5))
plt.hist(longueurs, bins=range(1, 61), color="#6B1420")
plt.title("Longueur des phrases du corpus")
plt.xlabel("Nombre de mots dans la phrase")
plt.ylabel("Nombre de phrases")
plt.tight_layout()
plt.savefig("resultats/longueur_phrases.png")
plt.close()