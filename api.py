import requests


u = 'https://python.gel.ulaval.ca/quoridor/api/'


def lister_parties(idul):
    rep = requests.get(u+'lister/', params={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        if 'message' in rep.keys():
            raise RuntimeError(rep['message'])
        return rep['parties']
    print(f"Le GET sur {u+'lister/'} a produit le code d'erreur {rep.status_code}.")


def débuter_partie(idul):
    rep = requests.post(u+'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        if 'message' in rep.keys():
            raise RuntimeError(rep['message'])
        return (rep['id'], rep['état'])
    print(f"Le POST sur {u+'débuter/'} a produit le code d'erreur {rep.status_code}.")


def jouer_coup(id_partie, type_coup, position):
    rep = requests.post(u+'jouer/', data={'id': id_partie, 'type' : type_coup,
'pos' : position})
    if rep.status_code == 200:
        rep = rep.json()
        if 'gagnant' in rep.keys():
            raise StopIteration(rep['gagnant'])
        if 'message' in rep.keys():
            raise RuntimeError(rep['message'])
        return rep['état']
    print(f"Le POST sur {u+'jouer/'} a produit le code d'erreur {rep.status_code}.")