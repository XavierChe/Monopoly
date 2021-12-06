import random
import affichage as aff
from propriete import *
from player import *
from luck import *

def read_properties(file):
    list_properties = []
    with open(file, "r") as f:
        lines = f.readlines()
    split_lines = []
    for i in range(len(lines)):
        split_lines.append(lines[i].split(" "))
        for j in range(1,7):
            split_lines[len(split_lines)-1][j] = int(split_lines[len(split_lines)-1][j])
    for i in range(len(split_lines)):
        list_properties.append(Property(*split_lines[i]))
    return list_properties

class Board:
    def __init__(self, debug: bool):
        if debug:  # create a debug board with only 4 spaces
            self._cases = []
            for k in range(5):
                name = "Property_nb_" + str(k)
                self._cases.append(Property(name, 0, 100))
            self._nb_spaces = 5
        else:
            # Plus complexe parce qu'il faut différencier toutes les cases
            # Mettre le bon nom de fichier puis ne plus y toucher
            properties = read_properties("properties.txt")
            #self._cases.append("Depart")
            self._cases = ["Start"]
            c=0
            for i in range(1,40):
                if (i==2 or i==7 or i==17 or i==22 or i==33 or i==36):
                    self._cases.append(Luck())
                elif (i==4 or i==38):
                    self._cases.append("Taxes")
                elif (i==10):
                    self._cases.append("Prison")
                elif (i==20):
                    self._cases.append("Free_Park")
                elif (i==30):
                    self._cases.append("Go_to_Prison")
                elif (i==12 or i==28):
                    self._cases.append(Company())
                else:
                    self._cases.append(properties[c])
                    c+=1

            self._nb_spaces = 40

    ## Accesseurs ##
    def cases(self):
        return self._cases
    
    def nb_spaces(self):
        return self._nb_spaces

    ## Méthodes ##

    def buy_property(self, player: Player):
        """Un joueur veut acheter une propriété. Aucun return mais fait des print et màj des données des propriétés et du joueur"""
        value=self.cases()[player.position()].value()
        if (player.money()<value):
            print("\n You don't have enough money to buy the property")
        else:
            player.set_money(player.money()-value)
            self.cases()[player.position()].set_owner(player.id())
            print("You now own ", self.cases()[player.position()].name(), "\n")

    def is_owned(self, id_space):
        """Renvoie l'ID du joueur si la propriété située sur id_space a été achetée et None sinon"""
        potential_owner=self.cases()[id_space].owner()
        if (potential_owner==0):
            return None
        else:
            return potential_owner

    def list_property(self, player: Player):
        """retourne la liste des propriétes que possède un joueur"""
        player_properties=[]
        for i in range(1,len(self.cases())):
            if (self.is_owned(i)==player.id()):
                player_properties.append(self.cases()[i])
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
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_result=dice_1+dice_2
        print(" You've got ", dice_result, "\n")
        if (player.position()+dice_result>=self.game_board.nb_spaces()):
            player.set_money(player.money()+200)
        if (player.position()+dice_result==40):
            player.set_money(player.money() + 200)
        player.set_position((player.position() + dice_result) % self.game_board.nb_spaces())
        print("You're now on - ", self.game_board.cases()[player.position()].name(), " - \n \n")
        if (self.game_board.cases()[player.position()]=="Property"):
            if (self.game_board.is_owned(player.position()) == player.id()):
                print(" Welcome Home !!!")
            elif self.game_board.is_owned(player.position()) is not None:
                id_of_owner = self.game_board.is_owned(player.position())
                print(" You must pay a tax to the other player")
                self.game_board.transaction(player, self.players[id_of_owner], 50)
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
        elif (self.game_board.cases()[player.position()]=="Depart"):
            print("You are at the start !!\n")
        elif(self.game_board.cases()[player.position()]=="Free_Park"):
            print("You are at the free park !!\n")
        elif(self.game_board.cases()[player.position()]=="Go_to_Prison"):
            print("How unlucky... You're imprisonned...\n")

        elif (self.game_board.cases()[player.position()].type()=="Luck"):
            self.game_board.cases()[player.position()].action()
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
            aff.clear_console()
            print(aff.manette_char)
            print("\n \n \n #### END OF DEBUG SESSION #### \n \n \n")


if __name__ == '__main__':
    new_game = Game(True)
    first_player = new_game.begin_game()
    if first_player == 1:
        order = [1, 2]
    elif first_player == 2:
        order = [2, 1]
    while (new_game.players[1].money() * new_game.players[2].money() >= 0 and first_player != None):
        new_game.player_tour(new_game.players[order[0]], new_game)
        new_game.player_tour(new_game.players[order[1]], new_game)
    new_game.end_game(True)

    # Flask, Pyramid, DJango
