import random
from collections import defaultdict

lettres = ['a', 'à', 'â', 'æ', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f', 'g', 'h', 'i', 'î', 'ï', 'j', 'k', 'l', 'm', 'n', 'o', 'ô', 'œ', 'p', 'q', 'r', 's', 't', 'u', 'ù', 'û', 'ü', 'v', 'w', 'x', 'y', 'ÿ', 'z']

# Créer une matrice pour stocker les occurrences
lettre = {}
occurrence = defaultdict(lambda: defaultdict(int))

#[[0 for _ in range(len(lettres))] for _ in range(len(lettres))]
# Fonction pour vider un tableau
def vide(T):
    T.clear()
    return T

# Lire les mots depuis le fichier
with open('liste.de.mots.francais.frgut.txt', 'r', errors='ignore') as m:
    lignes = m.readlines()
    for mot in lignes:
        for i in range(0, len(mot) -1 ,1):
            index_i = mot[i]
            index_j = mot[i + 1]
            occurrence[index_i][index_j] += 1

# Afficher la matrice des occurrences

print(occurrence)
for lettre1, suivie in occurrence.items():
    for lettre2, count in suivie.items():
        print(f"{lettre1} -> {lettre2}: {count}")
       