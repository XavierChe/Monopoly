from propriete import *
from player import *

def read_properties(file):
    list_properties=0
    return list_properties

class Board:
    def __init__(self):
        #Plus complexe parce qu'il faut différencier toutes les ptn de cases sa mère
        self._cases=[]
        #Mettre le bon nom de fichier puis ne plus y toucher
        properties=read_properties("Coucou")
        self.cases.append("Depart")
        for i in range(len(properties)):
            pass
    ## Accesseur ##
    def cases(self):
        return self._cases

    ## Méthodes ##

    def buy_property(self,player: Player):
        """Un joueur veut acheter une propriété. Aucun return mais fait des print et màj des données des propriétés et du joueur"""
        pass

    def rent_property(self, player: Player):
        """Un joueur tombe sur une case déjà possédée. Aucun return mais des print et màj des données des propriétés et du joueur"""
        pass

    def is_owner(self,player: Player):
        """Renvoie un booléen vrai si player est le propriétaie de la propriété"""
        pass

    def is_owned(self):
        """Renvoie un booléen indiquant si la propriété a été achetée ou non"""
        pass

class game:
    def __init__(self):
        pass

    def begin_game(self):
        pass

    def begin_tour(self):


    def actu_game(self):
        pass
