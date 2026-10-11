import os

DOSSIER_ENTREE = "donnees"
DOSSIER_SORTIE = "propre"
LETTRES_KURDES = set("êîûçş")

def ligne_kurde(ligne):
    for lettre in ligne.lower():
        if lettre in LETTRES_KURDES:
            return True
    return False


def nettoyer(texte):
    lignes = texte.split("\n")
    lignes = lignes[1:]
    gardees = []
    for ligne in lignes:
        ligne = ligne.strip()
        if ligne == "" or ligne.startswith("==") or "\\" in ligne or not ligne_kurde(ligne):
            continue
        gardees.append(ligne)
    return "\n".join(gardees)


os.makedirs(DOSSIER_SORTIE, exist_ok=True)

for nom in sorted(os.listdir(DOSSIER_ENTREE)):
    with open(os.path.join(DOSSIER_ENTREE, nom), encoding="utf-8") as fichier:
        texte = fichier.read()
    texte_propre = nettoyer(texte)
    with open(os.path.join(DOSSIER_SORTIE, nom), "w", encoding="utf-8") as fichier:
        fichier.write(texte_propre)
    print(nom, "nettoyé")