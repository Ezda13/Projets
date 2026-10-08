# Source : Haig, Geoffrey. « Northern Kurdish (Kurmanjî) », section 2.1 (phonologie).
# https://doi.org/10.1515/9783110421682-004

# Table de correspondance : lettre kurmancî avec API

TABLE = {
    "a": "aː", "b": "b", "c": "dʒ", "ç": "tʃ", "d": "d",
    "e": "æ", "ê": "eː", "f": "f", "g": "ɡ", "h": "h",
    "i": "ɨ", "î": "iː", "j": "ʒ", "k": "k", "l": "l",
    "m": "m", "n": "n", "o": "o:", "p": "p", "q": "q",
    "r": "ɾ", "s": "s", "ş": "ʃ", "t": "t", "u": "ʊ",
    "û": "uː", "v": "v", "w": "w", "x": "x", "y": "j",
    "z": "z",
}


def transcription(mot):
    mot = mot.lower()
    resultat = ""
    for position, lettre in enumerate(mot):
        if lettre == "r" and position == 0:
            resultat += "r"
        else:
            resultat += TABLE.get(lettre, lettre)
    resultat = resultat.replace("xw", "xʷ")
    return "[" + resultat + "]"


while True:
    mot = input("Mot en kurmancî (Entrée pour quitter) : ")
    if mot == "":
        break
    print(transcription(mot))
