import networkx as nx


class Quoridor:

    def __init__(self, joueurs, murs=None):
        self.joueurs = joueurs
        self.murs = murs


        if len(self.joueurs) > 2:
            raise QuoridorError('Le nombre de joueurs doit être 2.')

        if self.joueurs[0]['murs'] > 10 or self.joueurs[1]['murs'] > 10:
            raise QuoridorError('Le nombre maximal de murs est 10.')

        if self.joueurs[0]['murs'] < 0 or self.joueurs[1]['murs'] < 0:
            raise QuoridorError('Le nombre de murs doit être positif.')

        if type(self.murs) != dict:
            raise QuoridorError('Le paramètre "murs" doit être un dictionnaire.')

    def __str__(self):
        premiere_ligne = 'Légende: 1=' + self.joueurs[0]['nom'] + ', '
        premiere_ligne += '2=' + self.joueurs[1]['nom'] + '\n' + '   ' + '-'*35 + '\n'
        plateau = [['.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ',
                    ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ',
                    ' ', ' ', '.', ' | ', '\n', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|',
                    '\n'] for i in range(9)]
        plateau[8 - self.joueurs[0]['pos'][1] + 1][(self.joueurs[0]['pos'][0] - 1)*4] = '1'
        plateau[8 - self.joueurs[1]['pos'][1] + 1][(self.joueurs[1]['pos'][0] - 1) * 4] = '2'

        for i in range(9):
            plateau[i].insert(0, str(9-i) + ' | ')

        plateau.append(['--|-----------------------------------\n'])
        plateau.append([' ', ' ', '| ', '1', '   2',
                        '   3', '   4', '   5', '   6', '   7', '   8', '   9'])
        plateau[8] = plateau[8][:36]

        for pos in self.murs['horizontaux']:
            x, y = pos
            for i in range(7):
                plateau[9-y][35 + x*4 + i] = '-'

        for pos in self.murs['verticaux']:
            x, y = pos
            plateau[9-y-1][x*4 - 5] = '|'
            plateau[9-y-1][34 + x*4] = '|'
            plateau[9-y][x*4 - 5] = '|'

        return(premiere_ligne + ''.join(''.join(i for i in ligne) for ligne in plateau) + '\n')

    def déplacer_jeton(self, joueur, position):
        self.joueur = joueur
        self.position = position

        if joueur == 1:
            self.joueurs[0]['pos'] = (position[0], position[1])

        if joueur == 2:
            self.joueurs[1]['pos'] = (position[0], position[1])
        else:
            raise QuoridorError('Le numéro du joueur doit être "1" ou "2".')

        if not 1<= position[0] <=9:
            raise QuoridorError('Position invalide en x')

        if not 1<= position[1] <=9:
            raise QuoridorError('Position invalide en y')

        

    def état_partie(self): pass

    def jouer_coup(self, joueur): pass

    def partie_terminée(self): pass

    def placer_mur(self, joueur: int, position: tuple, orientation: str): pass


class QuoridorError(Exception): pass

joueurs = [{'nom': 'marc', 'murs': 10, 'pos': (5, 1)},
                {'nom': 'robot', 'murs': 10, 'pos': (5, 9)}]

murs = {'horizontaux': [(2, 3), (4, 4)], 'verticaux': [(6, 3)]}

y = Quoridor(joueurs, murs)
y.déplacer_jeton(2, (-1, 5))

print(y)