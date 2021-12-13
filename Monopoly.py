import random
import affichage as aff
from propriete import *
from player import *

def read_properties(file):
    list_properties = []
    with open(file, "r") as f:
        lines = f.readlines()
    split_lines = []
    for i in range(1,len(lines)):
        split_lines.append(lines[i].split(" "))
        for j in range(1,6):
            split_lines[len(split_lines)-1][j] = int(split_lines[len(split_lines)-1][j])
        split_lines[len(split_lines)-1][6] = [int(split_lines[len(split_lines)-1][i]) for i in range(6,12)]
    for i in range(len(split_lines)):
        list_properties.append(Property(*split_lines[i][:7]))
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
            self._cases = [Case("Start",0)]
            c=0
            for i in range(1,40):
                if (i==2 or i==7 or i==17 or i==22 or i==33 or i==36):
                    self._cases.append(Luck(i))
                elif (i==4):
                    self._cases.append(Taxes(i,100))
                elif(i==38):
                    self._cases.append(Taxes(i, 200))
                elif (i==10):
                    self._cases.append(Prison())
                elif (i==20):
                    self._cases.append(Case("Free Park",i))
                elif (i==30):
                    self._cases.append(GoToPrison())
                elif (i==12):
                    self._cases.append(Company(i,"Companie des eaux"))
                elif (i==28):
                    self._cases.append(Company(i,"Companie d'électricité"))
                elif (i==5):
                    self._cases.append(TrainStation("Gare Montparnasse",i))
                elif (i==15):
                    self._cases.append(TrainStation("Gare de Lyon",i))
                elif (i==25):
                    self._cases.append(TrainStation("Gare du Nord",i))
                elif (i==35):
                    self._cases.append(TrainStation("Gare Saint Lazare", i))
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
            print("\n You now own ", self.cases()[player.position()].name(), "\n")

    def is_owned(self, id_space):
        """Renvoie l'ID du joueur si la propriété située sur id_space a été achetée et None sinon"""
        potential_owner=self.cases()[id_space].owner()
        if (potential_owner==0):
            return None
        else:
            return potential_owner
        
    def ids_same_monopole(self, id_mono):
        ids = []
        cases = self.cases()
        for i in range(len(cases)):
            if cases[i].type() == "Property" and cases[i].monopole_id() == id_mono:
                ids.append(cases[i].id())
        return ids

    def list_property(self, player: Player):
        """retourne la liste des propriétes que possède un joueur"""
        player_properties=[]
        for i in range(1,len(self.cases())):
            if(self.cases()[i].type() in ["Property","Company","Train Station"]):
                if (self.is_owned(i) == player.id()):
                    player_properties.append(self.cases()[i])
        return player_properties

    def transaction(self, giver: Player, receiver: Player, amount_of_money: int):
        giver.set_money(giver.money()-amount_of_money)
        receiver.set_money(receiver.money()+amount_of_money)

class Game:
    def __init__(self, debug=False,nb_players = 2):
        """Initialise le board et les joueurs"""
        if debug:
            print("\n \n \n #### BEGINNING OF THE DEBUG SESSION #### \n \n \n")
            answer = input("")
            aff.clear_console()
            self.players = [0,Player(1),Player(2)]
            self.game_board = Board(True)
        else:
            aff.clear_console()
            self.players = [0]
            for i in range (1,nb_players+1):
                print(" Write the name of the player created : \n ")
                player_name=input("")
                self.players.append(Player(i,player_name))
            self.game_board = Board(False)

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
        print(" Time for ", player.name(), "to play !!! \n\n")
        print("██████████████████████████████████████████")
        print("\n Your Bank account : ", player.money(), " € \n \n")
        print(" Properties : \n")
        property_player = self.game_board.list_property(player)
        for i in range(1,len(property_player)+1):
            if (property_player[i-1].type()=="Property"):
                print(" ", i," - ", property_player[i-1].name(), " - Number of houses : ",property_player[i-1].nb_houses() , "\n")
            else:
                print(" ", i, " - ", property_player[i - 1].name(), "\n")
        print("██████████████████████████████████████████")
        ## b est un booléen pour déterminer si le joueur peut lancer les dés pour avancer
        b=True
        ## Cas Prison ##

        if (player.free()==False):
            if (player.escape_card()>0):
                print(" You have an escape card, you can leave the prison for free. \n")
                player.set_free(True)
                player.set_escape_card(player.escape_card()-1)
            else :
                print("You are imprisonned. \n Do you want to roll the dices to try to exit the prison this round ? \n")
                print("A- Yes \n \nB- No \n \n ")
                answer = ""
                while (answer != "A" and answer != "B"):
                    answer = input("")
                if answer == "B":
                    b = self.game_board.cases()[player.position()].rounds_passed(player)
                else:
                    print("\n Press enter to role the dices \n \n")
                    answer = input("")
                    dice_1 = random.randint(1, 6)
                    dice_2 = random.randint(1, 6)
                    print(" You've got ", dice_1, " and ", dice_2, "\n")
                    b = self.game_board.cases()[player.position()].trying_to_escape_prison(dice_1, dice_2, player)

        ## Cas possibilité d'avancer ##

        if(b):
            print("\n Press enter to roll the dices \n \n")
            answer = input("")
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            dice_result = dice_1 + dice_2
            print(" You've got", dice_1, "+", dice_2, "\n")
            if (player.position() + dice_result > self.game_board.nb_spaces()):
                player.set_money(player.money() + 200)
                print(" You passed the Start ! You receive 200€ ! \n \n")
            if (player.position() + dice_result == self.game_board.nb_spaces()):
                player.set_money(player.money() + 400)
                print(" You're exactly at the Start ! You receive 400€ ! \n \n")
            player.set_position((player.position() + dice_result) % self.game_board.nb_spaces())

            ## Cas départ ##
            if (self.game_board.cases()[player.position()].type() == "Start"):
                print(" You are at the start !!\n")

            ## Cas Parc Gratuit ##
            elif (self.game_board.cases()[player.position()].type() == "Free Park"):
                print(" You're now on - ", self.game_board.cases()[player.position()].type(), " - \n \n")
                print(" You are at the free park !!\n")

            ## Cas Simple visite en Prison ##
            elif(self.game_board.cases()[player.position()].type() == "Prison"):
                print(" You're now on - ", self.game_board.cases()[player.position()].type(), " - \n \n")
                print(" You are just visiting the prison \n \n")

            ## Cas Allez En Prison ##
            elif (self.game_board.cases()[player.position()].type() == "Go to Prison"):
                print(" You're now on - ", self.game_board.cases()[player.position()].type(), " - \n \n")
                print(" How unlucky... You're imprisonned...\n")
                self.game_board.cases()[player.position()].imprison(player)

            ## Cas Chance ##
            elif (self.game_board.cases()[player.position()].type() == "Luck"):
                print(" You're now on - ", self.game_board.cases()[player.position()].type(), " - \n \n")
                self.game_board.cases()[player.position()].action(player)

            ## Cas Taxes ##
            elif (self.game_board.cases()[player.position()].type() == "Taxes"):
                print(" You're now on - ", self.game_board.cases()[player.position()].type(), " - \n \n")
                print(" Oh nooooo, you have to pay taxes... It costs ", self.game_board.cases()[player.position()].value(), "€")
                self.game_board.cases()[player.position()].pay(player)

            ## Cas Compagnies, Gares et Propriétés ##
            if (self.game_board.cases()[player.position()].type() in ["Company","Train Station","Property"]):
                print(" You're now on - ", self.game_board.cases()[player.position()].name(), " - \n \n")
                if (self.game_board.is_owned(player.position()) == player.id()):
                    print(" Welcome Home !!!")
                elif self.game_board.is_owned(player.position()) is not None:
                    id_of_owner = self.game_board.is_owned(player.position())
                    print(" You must pay a tax to player ", id_of_owner, "\n \n")

                    ## Cas Companie ##
                    if(self.game_board.cases()[player.position()].type()=="Company"):
                        if (self.game_board.is_owned(12) == self.game_board.is_owned(28)):
                            print(" The rent is 10 times the sum of the value on the dices \n \n")
                            self.game_board.transaction(player, self.players[id_of_owner], 12 * dice_result)
                        else:
                            print(" The rent is 4 times the sum of the value on the dices \n \n")
                            self.game_board.transaction(player, self.players[id_of_owner], 4 * dice_result)

                    ## Cas Gare ##
                    elif(self.game_board.cases()[player.position()].type()=="Train Station"):
                        nb_train_stations_owned = 0
                        for i in range(5, 36, 10):
                            if (self.game_board.is_owned(i) == id_of_owner):
                                nb_train_stations_owned += 1
                        print(" It costs ", self.game_board.cases()[player.position()].rent(nb_train_stations_owned),
                              "€", "\n \n")
                        self.game_board.transaction(player, self.players[id_of_owner],
                                                    self.game_board.cases()[player.position()].rent(
                                                        nb_train_stations_owned))

                    ## Cas Propriété ##
                    else:
                        print(" It costs ", self.game_board.cases()[player.position()].rent(), "€", "\n \n")
                        self.game_board.transaction(player, self.players[id_of_owner],
                                                    self.game_board.cases()[player.position()].rent())
                else:
                    print(" Free space, you can buy the property \n \n")
                    print(" It costs ",self.game_board.cases()[player.position()].value(), "€", "\n \n")
                    print(" Do you want to buy it ? \n A- Yes \n B- No")
                    answer = ""
                    while (answer != "A" and answer != "B"):
                        answer = input("")
                    if answer == "A":
                        self.game_board.buy_property(player)
                    else:
                        pass


        print("\n \n Here is a brief recap of your situation : \n \n")
        print("██████████████████████████████████████████")
        print("\n Your Bank account : ", player.money(), " € \n \n")
        print(" Properties : \n")
        property_player = self.game_board.list_property(player)
        for i in range(1, len(property_player) + 1):
            if (property_player[i - 1].type() == "Property"):
                print(" ", i, " - ", property_player[i - 1].name(), " - Number of houses : ",
                      property_player[i - 1].nb_houses(), "\n")
            else:
                print(" ", i, " - ", property_player[i - 1].name(), "\n")
        print("██████████████████████████████████████████")
        if (len(property_player)>0):
            answer = ""
            while (answer != "B"):
                print("\n \n Do you want to display information about one of your properties ? (Does not work for train stations or companies) \n A- Yes \n B- No")
                answer = input("")
                if answer == "A":
                    print(" \n Which property ? Enter the id diplayed in the recap : \n \n")
                    id_property = int(input(""))
                    if (id_property < 1 or id_property > len(property_player) or property_player[
                        id_property-1].type() != "Property"):
                        print(" The number you entered is invalid")
                    else:
                        property_player[id_property-1].print_information()
            answer = ""
            while(answer!="B"):
                print(" \n \n Do you want to build a house ? \n A - Yes \n B - No")
                answer = input("")
                if answer == "A":
                    pass


        print("\n \n This is the end of your turn \n \n")
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
    print("\n \n Choose the number of players \n \n")
    nb_players=int(input(""))
    new_game = Game(False,nb_players)
    id_current_player = random.randint(1,nb_players)
    while (new_game.players[1].money() * new_game.players[2].money() >= 0):
        if (id_current_player>nb_players):
            id_current_player=1
        new_game.player_tour(new_game.players[id_current_player], new_game)
        id_current_player+=1
    new_game.end_game(True)
