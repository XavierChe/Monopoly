import random
import affichage as aff
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

    def list_property(self,player:Player):
        """retourne la liste des propriétes que possède un joueur"""
        pass

class Game:
    def __init__(self):
        """initialise le plateau et les joueurs"""
        pass

    def begin_game(self):
        """A method that is used in the very beginning of the game to start it
            It includes :
            -> The Game title page
            @Return the first player to play (an int between 1 and 2)"""
        aff.build_title(aff.letter,aff.nb_line,aff.nb_column)
        test_begin = input("")
        first_player = random.randint(1,2)
        return first_player

    def begin_tour(self,player:Player,board:Board):
        """Un tour de jeu pour un joueur"""
        print("Cest au tour du Joueur ",player.id(), "de jouer !!! \n\n")
        print("=======================================")
        print("Richesse Actuelle : ",player.money,"\n")
        print("Propriétés : \n")
        property_player = board.list_property(player)
        for property in property_player:
            print("-> ",property.name,"\n")
        print("=======================================")
        print("clique sur l'écran pour lancer les dés \n")


        #fonction qui attend le click (regarder commandes prompt)


        dice_result = random.randint(1,12)
        print("Tu as fait ",dice_result,"\n")
        player.set_position(player.position + dice_result) #Attention au retour au départ
        print("Tu es maintenant sur la case - ",board.cases[player.position].name," - \n")
        if (board.is_owner(player)):
            print("Tu es chez toi, il ne se passe donc rien !")
        elif(board.is_owned()):


            # Mecanisme de recherche et de paiement


            pass
        else:
            print("Case libre !!! tu peux acheter la propriété \n")


            # mécanisme d'achat


            pass
        print ("Fin du Tour. Passer au joueur suivant ? !!!")

    def end_game(self,player:Player):
        """The last method of the Game. It shows the winner and ends the game"""
        aff.build_end_page(player:Player)


    # Flask, Pyramid, DJango
