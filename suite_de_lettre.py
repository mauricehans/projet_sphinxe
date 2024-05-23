lettres = ['a', 'à', 'â', 'æ', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f', 'g', 'h', 'i', 'î', 'ï', 'j', 'k', 'l', 'm', 'n', 'o', 'ô', 'œ', 'p', 'q', 'r', 's', 't', 'u', 'ù', 'û', 'ü', 'v', 'w', 'x', 'y', 'ÿ', 'z']

# Créer une matrice pour stocker les occurrences
occurrence = [[0 for _ in range(len(lettres))] for _ in range(len(lettres))] 
# Fonction pour vider un tableau
def vide(T):
    T.clear()
    return T

# Lire les mots depuis le fichier
with open('liste.de.mots.francais.frgut.txt', 'r', errors='ignore') as m:
    lignes = m.readlines()

    for mot in lignes:
        mot = mot.strip()
        if len(mot) > 1:
            # Vider le tableau stock
            stock = vide([])

            # Ajouter les lettres du mot dans stock
            for lettre in mot:
                stock.append(lettre)

            # Vérification et comptage des occurrences
            for i in range(len(stock) - 1):
                if stock[i] in lettres and stock[i + 1] in lettres:
                    index_i = lettres.index(stock[i])
                    index_j = lettres.index(stock[i + 1])
                    occurrence[index_i][index_j] += 1

# Afficher la matrice des occurrences


for i in range(len(lettres)):
    for j in range(len(lettres)):
        print(f"{lettres[i]} -> {lettres[j]}: {occurrence[i][j]}")
       