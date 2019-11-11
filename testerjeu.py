
from main.py import *

def jouer_a_lejeu():
    idul = input('Quel est ton nom de joueur? ')
    etat = débuter_partie(idul)[1]
    identif = débuter_partie(idul)[0]

    while True:
        afficher_damier_ascii(etat)
        type_coup = input('Veux-tu jouer un mur ou un déplacement ? (entrez D, MH ou MV) ')
        position_x = int(input('Choisis une case en x :'))
        position_y = int(input('Choisis une case en y :'))
        etat = jouer_coup(identif, type_coup, (position_x, position_y))
        if 'gagnant' in etat.keys():
            continue
jouer_a_lejeu()