import random
from collections import defaultdict
# Créer une matrice pour stocker les occurrences

occurrence = defaultdict(lambda: defaultdict(int))

#[[0 for _ in range(len(lettres))] for _ in range(len(lettres))]
# Fonction pour vider un tableau

# Lire les mots depuis le fichier
with open('liste.de.mots.francais.frgut.txt', 'r', errors='ignore') as m:
    lignes = m.readlines()
    for mot in lignes:
        for i in range(0, len(mot) -1 ,1):
            index_i = mot[i]
            index_j = mot[i + 1]
            occurrence[index_i][index_j] += 1

# Afficher la matrice des probabiliter

for lettre1, suivie in occurrence.items():
    total_occurence = sum(suivie.values())
    for lettre2, count in suivie.items():
        occurrence[lettre1][lettre2] = count/ total_occurence
        #print(f"{lettre1} -> {lettre2}: {count/total_occurence}")
for j in range(0,10):
    premier_lettre = random.choice(list(occurrence.keys()))
    mot = [premier_lettre]
    probabiliter = 0
    for i in range (0,10,1):
        if probabiliter >= 1 :
            break
        else:
            liste_des_letter_probable = occurrence.get(premier_lettre, {})
            if not liste_des_letter_probable:
                break
            liste_lettre_suivie = list(liste_des_letter_probable.keys())
            liste_proba_suivie = list(liste_des_letter_probable.values())
            #choix d'une lettre
            nouvelle_lettre = random.choices(liste_lettre_suivie, liste_proba_suivie)[0]
            probabiliter += occurrence[premier_lettre][nouvelle_lettre]
            mot.append(nouvelle_lettre)
    print(''.join(mot))
