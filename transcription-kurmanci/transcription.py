# Source : Haig, Geoffrey. « Northern Kurdish (Kurmanjî) », section 2.1 (phonologie).
# https://doi.org/10.1515/9783110421682-004

import tkinter as tk

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


#interface

def transcrire(event=None):
    phrase = entree.get()
    resultat.config(text=transcription_phrase(phrase))



fenetre = tk.Tk()
fenetre.title("Transcription phonétique du kurmancî")

consigne = tk.Label(fenetre, text="Écris une phrase en kurmancî :", font=("Segoe UI", 12))
consigne.pack(padx=20, pady=(20, 5))

entree = tk.Entry(fenetre, width=40, font=("Segoe UI", 14))
entree.pack(padx=20)
entree.bind("<Return>", transcrire)

bouton = tk.Button(fenetre, text="Transcrire", command=transcrire)
bouton.pack(pady=10)

resultat = tk.Label(fenetre, text="", font=("Segoe UI", 16))
resultat.pack(padx=20, pady=(0, 20))

fenetre.mainloop()