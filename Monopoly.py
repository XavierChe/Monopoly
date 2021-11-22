import random
import affichage as aff
from propriete import *
from player import *

def read_properties(file):
    nb_spaces: int
    list_properties=0
    return list_properties


class Board:
    def __init__(self, debug: bool):
        if debug:  # create a debug board with only 4 spaces
            _cases = []
            for k in range(5):
                name = "Property_nb_" + str(k)
                _cases.append(Property(name))
            self.cases = _cases
            self.nb_spaces = 5
        else:
            # Plus complexe parce qu'il faut différencier toutes les ptn de cases sa mère
            self._cases = []
            # Mettre le bon nom de fichier puis ne plus y toucher
            properties = read_properties("Coucou")
            self.cases.append("Depart")
            for i in range(len(properties)):
                pass

    ## Accesseur ##
    def cases(self):
        return self._cases

    ## Méthodes ##

    def buy_property(self, player: Player):
        """Un joueur veut acheter une propriété. Aucun return mais fait des print et màj des données des propriétés et du joueur"""
        value=self.cases[player.position()].value()
        if (player.money()<value):
            print("You don't have enough money to buy the property")
        else:
            player.set_money(player.money()-value)
            self.cases[player.position()].set_owner(player.id())
            print("You now own ",self.cases[player.position()].name,"\n")

    def is_owned(self, id_space):
        """Renvoie l'ID du joueur si la propriété située sur id_space a été achetée et None sinon"""
        potential_owner=self.cases[id_space].owner()
        if (potential_owner==0):
            return None
        else:
            return potential_owner

    def list_property(self, player: Player):
        """retourne la liste des propriétes que possède un joueur"""
        player_properties=[]
        for i in range(1,len(self.cases)):
            if (self.is_owned(i)==player.id()):
                player_properties.append(self.cases[i])
        return player_properties

    def transaction(self, giver: Player, receiver: Player, amount_of_money: int):
        giver.set_money(giver.money()-amount_of_money)
        receiver.set_money(receiver.money()+amount_of_money)



class Game:
    def __init__(self, debug=False):
        """Initialise le board et les joueurs"""
        if debug:
            print("\n \n \n #### BEGINNING OF THE DEBUG SESSION #### \n \n \n")
            answer = input("")
            aff.clear_console()
            self.players = [0,Player(1),Player(2)]
            self.game_board = Board(True)

    def test_game(self):
        """Effectue divers test sur le bon fonctionnement du jeu"""
        pass

    def begin_game(self):
        """A method that is used in the very beginning of the game to start it
            It includes :
            -> The Game title page
            @Return the first player to play (an int between 1 and 2)"""
        aff.clear_console()  # clear the page
        print(aff.manette_char)  # print an image of a controller
        print(aff.monopoly_char)  # print the name of the game
        print("\n \n \n \n \n")
        print("         A- New Game \n \n         B- Exit \n \n ")
        answer = ""
        while (answer != "A" and answer != "B"):
            answer = input("");
        if answer == "B":
            return None
        aff.clear_console()
        print(aff.manette_char)  # print an image of a controller
        print(aff.monopoly_char)  # print the name of the game
        first_player_index = random.randint(1, 2)
        print("\n \n \n \n \n The game will start with player ", first_player_index)
        print("\n \n Press Enter to start")
        answer = input("")
        return first_player_index

    def player_tour(self, player: Player, board: Board):
        """Un tour de jeu pour un joueur"""
        aff.clear_console()
        print(aff.monopoly_char)
        print("\n \n \n \n")
        print(" Time for player ", player.id(), "to play !!! \n\n")
        print("██████████████████████████████████████████")
        print("\n Your Bank account : ", player.money(), " € \n \n")
        print(" Properties : \n")
        property_player = self.game_board.list_property(player)
        for property in property_player:
            print("-> ", property.name(), "\n")
        print("██████████████████████████████████████████")
        print("\n Press enter to role the dices \n \n")
        answer = input("")
        dice_result = random.randint(1, 12)
        print(" You've got ", dice_result, "\n")
        player.set_position((player.position() + dice_result) % self.game_board.nb_spaces)
        print("You're now on - ", self.game_board.cases[player.position()].name(), " - \n \n")
        if (self.game_board.is_owned(player.position())==player.id()):
            print(" Welcome Home !!!")
        elif self.game_board.is_owned(player.position()) is not None:
            id_of_owner = self.game_board.is_owned(player.position())
            print(" You must pay a tax to the other player")
            self.game_board.transaction(player.id, id_of_owner, player.position)
        else:
            print(" Free space, you can own the property \n \n")
            print(" Do you want to buy it ? \n A- Yes \n B- No")
            answer = ""
            while (answer != "A" and answer != "B"):
                answer = input("")
            if answer == "A":
                self.game_board.buy_property(player)
            else:
                pass
        print("\n \n This is the end of your tour. Here is a brief recap of your situation : \n \n")
        print("██████████████████████████████████████████")
        print("\n Your Bank account : ", player.money(), " € \n \n")
        print(" Properties : \n")
        property_player = self.game_board.list_property(player)
        for property in property_player:
            print("  -> ", property.name(), "\n")
        print("██████████████████████████████████████████")
        print("\n Press enter to continue \n \n")
        answer = input("")
        return None

    def end_game(self, debug: bool):
        """The last method of the Game. It shows the winner and ends the game"""
        if debug:
            print("\n \n \n #### END OF DEBUG SESSION #### \n \n \n")


if __name__ == '__main__':
    new_game = Game(True)
    first_player = new_game.begin_game()
    if first_player == 1:
        new_game.player_tour(new_game.player1, new_game)
    elif first_player == 2:
        new_game.player_tour(new_game.player2, new_game)
    new_game.end_game(True)

    # Flask, Pyramid, DJango
