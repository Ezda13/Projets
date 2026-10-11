import os
import re

DOSSIER = "propre"
ALPHABET = set("abcçdeêfghiîjklmnopqrsştuûvwxyz")
UNE_LETTRE = set("ûêaeî")


def lire_corpus():
    textes = []
    for nom in sorted(os.listdir(DOSSIER)):
        with open(os.path.join(DOSSIER, nom), encoding="utf-8") as fichier:
            textes.append(fichier.read())
    return "\n".join(textes)


def est_kurmanci(mot):
    if len(mot) == 1 and mot not in UNE_LETTRE:
        return False
    for lettre in mot:
        if lettre not in ALPHABET:
            return False
    return True


def decouper_mots(texte):
    mots = re.findall(r"[^\W\d_]+", texte.lower())
    gardes = []
    for mot in mots:
        if est_kurmanci(mot):
            gardes.append(mot)
    return gardes


def decouper_phrases(texte):
    morceaux = re.split(r"[.!?]+", texte)
    phrases = []
    for morceau in morceaux:
        morceau = morceau.strip()
        if morceau != "":
            phrases.append(morceau)
    return phrases


if __name__ == "__main__":
    corpus = lire_corpus()
    mots = decouper_mots(corpus)
    phrases = decouper_phrases(corpus)
    print("Nombre de mots :", len(mots))
    print("Nombre de mots différents :", len(set(mots)))
    print("Nombre de phrases :", len(phrases))
    print("Les 20 premiers mots :", mots[:20])