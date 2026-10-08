# Source : Haig, Geoffrey. « Northern Kurdish (Kurmanjî) », section 2.1 (phonologie).
# https://doi.org/10.1515/9783110421682-004

# Table de correspondance : lettre kurmancî avec API

TABLE = {
    "a": "aː", "b": "b", "c": "dʒ", "ç": "tʃ", "d": "d",
    "e": "æ", "ê": "eː", "f": "f", "g": "ɡ", "h": "h",
    "i": "ɨ", "î": "iː", "j": "ʒ", "k": "k", "l": "l",
    "m": "m", "n": "n", "o": "oː", "p": "p", "q": "q",
    "r": "ɾ", "s": "s", "ş": "ʃ", "t": "t", "u": "ʊ",
    "û": "uː", "v": "v", "w": "w", "x": "x", "y": "j",
    "z": "z",
}


def transcription_mot(mot):
    mot = mot.lower()
    resultat = ""
    for position, lettre in enumerate(mot):
        if lettre == "r" and position == 0:
            resultat += "r"
        else:
            resultat += TABLE.get(lettre, lettre)
    resultat = resultat.replace("xw", "xʷ")
    return resultat

def transcription_phrase(phrase):
    mots = phrase.split()
    transcrits = [] 
    for mot in mots:
        transcrits.append(transcription_mot(mot))
    return "[" + " ".join(transcrits) +"]"


while True:
    phrase = input("Phrase en kurmancî (Entrée pour quitter) : ")
    if phrase == "":
        break
    print(transcription_phrase(phrase))
