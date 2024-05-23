import random
from collections import defaultdict
nombre = int(input("entre un nombre"))
lettres = ['a', 'à', 'â', 'æ', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f', 'g', 'h', 'i', 'î', 'ï', 'j', 'k', 'l', 'm', 'n', 'o', 'ô', 'œ', 'p', 'q', 'r', 's', 't', 'u', 'ù', 'û', 'ü', 'v', 'w', 'x', 'y', 'ÿ', 'z']

occurrence = defaultdict(lambda: defaultdict(int))

def vide(T):
    T.clear()
    return T
for i in range (nombre):
    # Lire les mots depuis le fichier
    with open('mots.txt', 'r', errors='ignore') as m:
        lignes = m.readlines()
        for mot in lignes:
            for i in range(0, len(mot) - 1):
                index_i = mot[i]
                index_j = mot[i + 1]
                occurrence[index_i][index_j] += 1

        for lettre1, suivie in occurrence.items():
            total_occurence = sum(suivie.values())
            for lettre2, count in suivie.items():
                occurrence[lettre1][lettre2] = count / total_occurence

    def choisir_premiere_lettre(occurrence):
        probs = []
        lettres = []
        total = 0
        for lettre, suivie in occurrence.items():
            occ_totale = sum(suivie.values())
            total += occ_totale
            probs.append(occ_totale)
            lettres.append(lettre)

        r = random.random()
        s = 0
        for i, p in enumerate(probs):
            s += p / total
            if r < s:
                return lettres[i]

    def choisir_lettre(lettre, occurrence):
        probs = list(occurrence[lettre].values())
        lettres = list(occurrence[lettre].keys())
        r = random.random()
        s = 0

        for i, p in enumerate(probs):
            s += p
            if r < s:
                
                return lettres[i]

    # Génération d'un mot aléatoire
    premiere_lettre = choisir_premiere_lettre(occurrence)
    mot = premiere_lettre
    longueur_mot = random.randint(3, 10)  # Longueur aléatoire entre 3 et 10 caractères

    for _ in range(longueur_mot - 1):
        lettre_suivante = choisir_lettre(mot[-1], occurrence)
        mot += lettre_suivante

    print(f"Mot aléatoire généré : {mot}") #None