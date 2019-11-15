import argparse


import api


def analyser_commande():
    """Analyser les commandes du terminal"""
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument('idul', metavar='idul', help="IDUL du joueur.")
    parser.add_argument('-l', '--lister', action='store_true',
                        help='Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()


def afficher_damier_ascii(dic):
    """Afficher le damier"""
    premiere_ligne = 'Légende: 1=' + dic['joueurs'][0]['nom'] + ', 2=' + dic['joueurs'][1]['nom'] + '\n' + '   ' + '-'*35 + '\n'
    plateau = [['.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ',
                ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ',
                ' ', ' ', '.', ' | ', '\n', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n'] for i in range(9)]
    plateau[8 - dic["joueurs"][0]['pos'][1] + 1][(dic["joueurs"][0]['pos'][0] - 1)*4] = '1'
    plateau[8 - dic["joueurs"][1]['pos'][1] + 1][(dic["joueurs"][1]['pos'][0] - 1) * 4] = '2'

    for i in range(9):
        plateau[i].insert(0, str(9-i) + ' | ')

    plateau.append(['--|-----------------------------------\n'])
    plateau.append([' ', ' ', '| ', '1', '   2',
                    '   3', '   4', '   5', '   6', '   7', '   8', '   9'])
    plateau[8] = plateau[8][:36]

    for pos in dic['murs']['horizontaux']:
        x, y = pos
        for i in range(7):
            plateau[9-y][35 + x*4 + i] = '-'

    for pos in dic['murs']['verticaux']:
        x, y = pos
        plateau[9-y-1][x*4 - 5] = '|'
        plateau[9-y-1][34 + x*4] = '|'
        plateau[9-y][x*4 - 5] = '|'

    print(premiere_ligne + ''.join(''.join(i for i in ligne) for ligne in plateau) + '\n')


def jouer():

    idul = analyser_commande().idul
    etat = api.débuter_partie(idul)[1]
    identif = api.débuter_partie(idul)[0]

    while True:
        try:
            afficher_damier_ascii(etat)
            type_coup = input('Quel est votre coup (D, MH ou MV) ?')
            position_x = input('Veuillez choisir une case en x :')
            position_y = input('Veuillez choisir une case en y :')
            etat = api.jouer_coup(identif, type_coup, (position_x, position_y))

        except RuntimeError as err:
            print(err)
            print('Veuillez reprendre votre coup')

        except StopIteration as err:
            print(f'{err} a gagné !')
            break

if analyser_commande().lister:
    print(api.lister_parties(analyser_commande().idul))
else:
    jouer()
