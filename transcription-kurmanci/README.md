# Transcription phonétique du kurmancî

Un outil en Python qui convertit une phrase écrit en kurmancî (kurde du Nord, alphabet latin) en transcription phonétique, selon l'alphabet phonétique international (API).

```
Phrase en kurmancî (Entrée pour quitter) : Ez kurd im
[æz kʊɾd ɨm]
Phrase en kurmancî (Entrée pour quitter) : xwesû
[xʷæsuː]
```

## Utilisation

Il faut Python 3. Depuis le dossier du projet :

```
python transcription.py
```

Tape un mot ou une phrase, puis Entrée. Pour quitter, appuie sur Entrée sans rien écrire.

## Fonctionnement

1. **Correspondance lettre par lettre** : chaque lettre de l'alphabet kurmancî est associée à un son de l'API.
2. **Règle du r** : un *r* en début de mot est roulé [r] ; ailleurs, il est noté battu [ɾ].
3. **Groupe xw** : il est transcrit [xʷ].
4. **Phrases** : la phrase est découpée en mots, chaque mot est transcrit séparément, puis les mots sont réunis entre crochets.

## Choix de transcription

- Les voyelles *a, ê, î, o, û* sont notées longues [ː]. Selon Haig, la longueur n'est pas distinctive en kurmancî, mais ces voyelles sont généralement réalisées longues.
- La transcription suit le kurmancî standard, fondé sur le parler de Cizre et Botan.

## Limites

- **Consonnes aspirées** : l'outil ne distingue pas les consonnes aspirées des non aspirées (p/pʰ, t/tʰ, k/kʰ, ç/tʃʰ). Cette opposition existe en kurmancî, mais l'orthographe ne la note pas et elle ne peut pas être prédite par des règles.
- **Le r à l'intérieur des mots** : il peut être roulé ou battu selon le mot (*pir* [pɨr] « beaucoup », *pir* [pɨɾ] « pont »). L'outil note toujours [ɾ].
- **Variation dialectale** : la prononciation varie selon les régions. L'outil ne la prend pas en compte.
- **Voyelles épenthétiques** : certains mots ont deux prononciations, avec ou sans voyelle ajoutée (*spî* [spiː] ~ [sɨpiː]). L'outil suit l'orthographe.
- **Ponctuation** : elle est recopiée telle quelle, collée au mot. Un mot précédé d'un signe (par exemple « ou un tiret) ne bénéficie pas de la règle du r en début de mot.

## Pistes d'amélioration

- Un lexique des mots à consonnes aspirées
- Une interface web

## Source

Haig, Geoffrey. « Northern Kurdish (Kurmanjî) », section 2.1 (phonologie). https://doi.org/10.1515/9783110421682-004
