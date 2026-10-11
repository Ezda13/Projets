# Table de correspondance : lettres simples
TABLE = {
    "ا": "a", "ب": "b", "پ": "p", "ت": "t", "ج": "c",
    "چ": "ç", "ح": "h", "خ": "x", "د": "d", "ر": "r",
    "ڕ": "ř", "ز": "z", "ژ": "j", "س": "s", "ش": "ş",
    "ع": "'", "غ": "x", "ف": "f", "ڤ": "v", "ق": "q",
    "ک": "k", "گ": "g", "ل": "l", "ڵ": "ł", "م": "m",
    "ن": "n", "ه": "h", "ە": "e", "ێ": "ê", "ۆ": "o",
    "ئ": "",
    # lettres ambiguës
    "و": "u", "ی": "î",
}


def convertir_mot(mot):
    mot = mot.replace("وو", "û")
    resultat = ""
    for lettre in mot:
        resultat += TABLE.get(lettre, lettre)
    return resultat


def convertir_texte(texte):
    mots_convertis = []
    for mot in texte.split():
        mots_convertis.append(convertir_mot(mot))
    return " ".join(mots_convertis)


if __name__ == "__main__":
    while True:
        texte = input("Texte en soranî (Entrée pour quitter) : ")
        if texte == "":
            break
        print(convertir_texte(texte))