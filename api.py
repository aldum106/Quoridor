import requests


def lister_parties(idul):
     url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
     rep = requests.get(url_base+'lister/', params={'idul': idul})
     if rep.status_code == 200:
         rep = rep.json()
         return rep['parties']
     else:
          raise RuntimeError(rep['message'])

def débuter_partie(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idul})
    if rep.status_code == 200:
         rep = rep.json()
         return (rep['id'], rep['état'])
    else:
         raise RuntimeError(rep['message'])

def jouer_coup(id_partie, type_coup, position):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'jouer/', data={'id': id_partie, 'type' : type_coup, 'pos' : position})
    if rep.status_code == 200:
         rep = rep.json()
         return rep['état']
    else:
         RuntimeError(rep['message'])

