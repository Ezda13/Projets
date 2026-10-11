# Convertisseur soranî (arabo-kurde) -> alphabet latin (Hawar)

Un outil qui translittère un texte soranî (kurde central, écrit en alphabet arabe) vers l'alphabet latin utilisé pour le kurmancî (kurde du Nord).

Les deux grands dialectes du kurde s'écrivent le plus souvent avec deux alphabets différents. En les mettant dans la même écriture, l'outil permet de comparer les deux dialectes mot à mot : vocabulaire, terminaisons, marques grammaticales.

Essayer l'outil en ligne : [ezda13.github.io/Projets/convertisseur-sorani](https://ezda13.github.io/Projets/convertisseur-sorani/)

## Fonctionnement

On écrit ou on colle un texte soranî dans la zone de saisie. Chaque mot apparaît ensuite sous forme de carte : le mot soranî en haut, sa translittération en dessous. Cette présentation interlinéaire, courante en linguistique, facilite la comparaison. La conversion se fait en direct, à chaque lettre tapée.

## Table de correspondance

Lettres à correspondance directe

| Soranî | Latin | Soranî | Latin | Soranî | Latin |
|---|---|---|---|---|---|
| ا | a | ژ | j | ل | l |
| ب | b | س | s | م | m |
| پ | p | ش | ş | ن | n |
| ت | t | ف | f | ه / ھ | h |
| ج | c | ڤ | v | ە | e |
| چ | ç | ق | q | ێ | ê |
| خ | x | ک | k | ۆ | o |
| د | d | گ | g | وو | û |
| ر | r | ز | z | | |

Lettres sans équivalent dans l'alphabet kurmancî

| Soranî | Son | Choix |
|---|---|---|
| ڕ | r roulé | ř |
| ڵ | l vélaire | ł |
| ع | consonne pharyngale | ' |
| ح | h pharyngal | h (sans distinction avec ه) |
| غ | r grasseyé | x (comme en kurmancî, par exemple xerîb) |
| ئ | support de voyelle | non transcrit |

## Règles

L'écriture soranî utilise و et ی à la fois comme consonnes (w, y) et comme voyelles (u, î). L'outil les distingue grâce à des règles fondées sur l'orthographe :

| Règle | Exemple |
|---|---|
| و et ی sont des consonnes en début de mot | وەک → wek, یەک → yek |
| … ou à côté d'une voyelle (ا, ە, ێ, ۆ) | سڵاو → sław, کوێ → kwê |
| … ou après î ou û | کوردیی → kurdîy |
| Sinon, ce sont des voyelles | کورد → kurd, شیر → şîr |
| و seul (la conjonction « et ») | و → û |
| وو suivi d'une voyelle | پێکهاتووە → pêkhatûwe |

Le support de voyelle ئ explique la première règle : sans lui, une lettre en début de mot serait lue comme une consonne (ئیمە → îme).

## Choix de translittération : le i bref

L'écriture arabe du soranî ne note pas le i bref (/ɨ/). L'outil ne le restitue pas : کوردستان devient kurdstan et non kurdistan.

Ce choix est volontaire :
- la translittération reste fidèle à ce qui est écrit, sans rien deviner ;
- elle est réversible : on pourrait reconvertir le texte latin en soranî sans perte ;
- elle reste lisible pour un locuteur du kurde.

## Limites

- Majuscules : l'alphabet arabe n'en a pas, donc les noms propres sont translittérés en minuscules.
- Distinctions perdues : ح et ه donnent tous deux h, غ et خ donnent tous deux x.
- Règles orthographiques : les règles sur و et ی couvrent les cas réguliers ; quelques mots peuvent leur échapper.
- Variantes Unicode : certains textes utilisent des lettres arabes (ي, ك) au lieu des lettres kurdes (ی, ک). Elles ne sont pas encore converties.

## Suite du projet

Une deuxième partie utilisera ce convertisseur pour comparer des textes soranî et kurmancî, par exemple des articles de Wikipédia publiés dans les deux dialectes.

## Utilisation

En ligne, via le lien ci-dessus, ou en ouvrant `index.html` dans un navigateur. Aucune installation n'est nécessaire.

## Autrice

Hülya Özen (Ezda), étudiante en Master de Traitement Automatique des Langues à l'INALCO. Portfolio : ezda13.github.io
