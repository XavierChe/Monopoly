from player import *
import random
import pygame
import pygame.locals as pl
from color import *
from text_input import Terminal
from propriete import Case, Property, Taxes, TrainStation, GoToPrison, Prison, Luck, Company
import time

pygame.init()


def text_format(message, textSize, textColor):
    newFont = pygame.font.SysFont("Consolas", textSize)
    newText = newFont.render(message, True, textColor)
    return newText


def read_properties(file):
    """Prend en entrée un fichier qui contient les informations des propriétés, renvoie une liste de Properties initialisées à l'aide du fichier"""
    list_properties = []
    with open(file, "r") as f:
        lines = f.readlines()
    split_lines = []
    for i in range(1, len(lines)):
        split_lines.append(lines[i].split(
            " "))  # On découpe les lignes du fichier (pour séparer les attributs) pour pouvoir définir les différentes propriétés
        for j in range(1, 7):
            split_lines[len(split_lines) - 1][j] = int(split_lines[len(split_lines) - 1][
                                                           j])  # Conversion en entiers des champs qui doivent être entiers (prix de la propriété, ...)
        split_lines[len(split_lines) - 1][7] = [int(split_lines[len(split_lines) - 1][i]) for i in
                                                range(7, 13)]  # Création de la liste des différents loyers
    for i in range(len(split_lines)):
        list_properties.append(Property(
            *split_lines[i][:8]))  # Initialisation de chaque propriété avec les informations données dans le fichier
    return list_properties


class Board:
    def __init__(self):
            # Plus complexe parce qu'il faut différencier toutes les cases
            # Mettre le bon nom de fichier puis ne plus y toucher
        properties = read_properties("properties.txt")
        self._cases = [Case("Start", 0)]
        c = 0
        for i in range(1, 40):
            if (i == 2 or i == 7 or i == 17 or i == 22 or i == 33 or i == 36):
                self._cases.append(Luck(i))
            elif (i == 4):
                self._cases.append(Taxes(i, 100))
            elif (i == 38):
                self._cases.append(Taxes(i, 200))
            elif (i == 10):
                self._cases.append(Prison())
            elif (i == 20):
                self._cases.append(Case("Free Park", i))
            elif (i == 30):
                self._cases.append(GoToPrison())
            elif (i == 12):
                self._cases.append(Company(i, "Companie des eaux"))
            elif (i == 28):
                self._cases.append(Company(i, "Companie d'électricité"))
            elif (i == 5):
                self._cases.append(TrainStation("Gare Montparnasse", i))
            elif (i == 15):
                self._cases.append(TrainStation("Gare de Lyon", i))
            elif (i == 25):
                self._cases.append(TrainStation("Gare du Nord", i))
            elif (i == 35):
                self._cases.append(TrainStation("Gare Saint Lazare", i))
            else:
                self._cases.append(properties[c])
                c += 1
            self._nb_spaces = 40

    ## Accesseurs ##
    def cases(self):
        return self._cases

    def nb_spaces(self):
        return self._nb_spaces

    ## Méthodes ##
    def buy_property(self, player: Player):
        """Un joueur veut acheter une propriété. Aucun return mais fait des print et màj des données des propriétés et du joueur"""
        value = self.cases()[player.position()].value()
        player.set_money(player.money() - value)
        self.cases()[player.position()].set_owner(player.id())
        print("\n You now own ", self.cases()[player.position()].name(), "\n")

    def is_owned(self, id_space):
        """Renvoie l'ID du joueur si la propriété située sur id_space a été achetée et None sinon"""
        potential_owner = self.cases()[id_space].owner()
        if (potential_owner == 0):
            return None
        else:
            return potential_owner

    def ids_same_monopole(self, id_mono):
        ids = []
        for i in range(len(self.cases())):
            if (self.cases()[i].type() == "Property" and self.cases()[i].monopole_id() == id_mono):
                ids.append(self.cases()[i].id())
        return ids

    def list_property(self, player: Player):
        """retourne la liste des propriétes que possède un joueur"""
        player_properties = []
        for i in range(1, len(self.cases())):
            if (self.cases()[i].type() in ["Property", "Company", "Train Station"]):
                if (self.is_owned(i) == player.id()):
                    player_properties.append(self.cases()[i])
        return player_properties

    def transaction(self, giver: Player, receiver: Player, amount_of_money: int):
        giver.set_money(giver.money() - amount_of_money)
        receiver.set_money(receiver.money() + amount_of_money)

    def houses_on_monopole(self, id_property):
        ids_monopole = self.ids_same_monopole(self.cases()[id_property].monopole_id())
        nb_house = 0
        for id in ids_monopole:
            if (self.cases()[id].nb_houses() > 0):
                nb_house += 1
        return nb_house

    def sell_property(self, player: Player, id_property):
        if (self.cases()[id_property].type == "Property"):
            if (self.houses_on_monopole(id_property) > 0):
                print(" \n \n You have to sell all the houses of the monopole before selling this property \n \n")
            else:
                self.cases()[id_property].set_owner(0)
                value = self.cases()[id_property].value()
                player.set_money(player.money() + value)
                print(" \n \n You earned ", value, "€ \n \n")
        else:
            self.cases()[id_property].set_owner(0)
            value = self.cases()[id_property].value()
            player.set_money(player.money() + value)
            print(" \n \n You earned ", value, "€ \n \n")


class Game_graph:
    def __init__(self, game_var):
        """Initialise le board et les joueurs"""
        nb_players = len(game_var) - 1
        self.players = [0]
        self.term = None
        self.screen = None
        for i in range(1, nb_players + 1):
            self.players.append(Player(i, game_var[i]))
            self.game_board = Board()

    def find_player(self, player_name):
        id_player = 0
        for i in range(1, len(self.players)):
            if self.players[i].name() == player_name:
                id_player = self.players[i].id()
        return id_player


    def display_properties(self, property_player,nb_line):
        for i in range(1, len(property_player) + 1):
            self.term.print_line(str(i) + " - " + property_player[i - 1].name(), nb_line + i - 1)
        return (nb_line + len(property_player))


    def exchange_properties(self, id_buyer, id_seller, value_exchange, id_property_buyer, id_property_seller):
        self.game_board.cases()[id_property_buyer].set_owner(id_seller)
        self.game_board.cases()[id_property_seller].set_owner(id_buyer)
        self.game_board.transaction(self.players[id_buyer], self.players[id_seller], value_exchange)


    def player_tour(self, player: Player):

        """Un tour de jeu pour un joueur"""
        self.term.clear_all()
        self.term.print_line("██████████████████████████████████████████", 1)
        self.term.print_line(" Time for " + str(player.name()) + " to play !!! ",2)
        self.term.print_line("Your Bank account : " + str(player.money()) + " € ",3)
        self.term.print_line("Properties : ",4)
        property_player = self.game_board.list_property(player)
        current_line = self.display_properties(property_player,5)
        current_line = self.term.print_line("██████████████████████████████████████████",current_line)
        ## b est un booléen pour déterminer si le joueur peut lancer les dés pour avancer
        b = True
        ## Cas Prison ##

        if (player.free() == False):
            if (player.escape_card() > 0):
                self.term.print_line(" You have an escape card, you can leave the prison for free",current_line)
                player.set_free(True)
                player.set_escape_card(player.escape_card() - 1)
            else:
                current_line = self.term.print_line("You are imprisonned. Do you want to roll the dices to try to exit the prison this round ?",current_line)
                current_line = self.term.print_line("A- Yes", current_line)
                current_line = self.term.print_line("B- No", current_line)
                output = self.term.print_input(current_line,lambda input: input=="A" or input =="B")
                current_line +=1
                if output == "B":
                    b = self.game_board.cases()[player.position()].rounds_passed(player)
                else:
                    current_line = self.term.print_line("Press enter to role the dices",current_line)
                    go = True
                    while go:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                go = False
                    dice_1 = random.randint(1, 6)
                    dice_2 = random.randint(1, 6)
                    current_line = self.term.print_line(" You've got " + str(dice_1) + " and " + str(dice_2), current_line)
                    b = self.game_board.cases()[player.position()].trying_to_escape_prison(dice_1, dice_2, player)

        ## Cas possibilité d'avancer ##

        if (b):
            current_line = self.term.print_line("Press enter to role the dices",current_line)
            go = True
            while go:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        go = False
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            dice_result = dice_1 + dice_2
            current_line = self.term.print_line(" You've got " + str(dice_1) + " and " + str(dice_2), current_line)
            if (player.position() + dice_result > self.game_board.nb_spaces()):
                player.set_money(player.money() + 200)
                current_line = self.term.print_line(" You passed the Start ! You receive 200€ !", current_line)
            if (player.position() + dice_result == self.game_board.nb_spaces()):
                player.set_money(player.money() + 400)
                current_line = self.term.print_line(" You're exactly at the Start ! You receive 400€ !", current_line)
            player.set_position((player.position() + dice_result) % self.game_board.nb_spaces())


            ## Cas départ ##
            if (self.game_board.cases()[player.position()].type() == "Start"):
                current_line = self.term.print_line(" You are at the start !!", current_line)

            ## Cas Parc Gratuit ##
            elif (self.game_board.cases()[player.position()].type() == "Free Park"):
                current_line = self.term.print_line(" You're now on - " + self.game_board.cases()[player.position()].type() , current_line)
                current_line = self.term.print_line(" You are at the free park !!", current_line)

            ## Cas Simple visite en Prison ##
            elif (self.game_board.cases()[player.position()].type() == "Prison"):
                current_line = self.term.print_line(" You're now on - " +  self.game_board.cases()[player.position()].type(), current_line)
                current_line = self.term.print_line(" You are just visiting the prison", current_line)

            ## Cas Allez En Prison ##
            elif (self.game_board.cases()[player.position()].type() == "Go to Prison"):
                current_line = self.term.print_line(" You're now on - " +  self.game_board.cases()[player.position()].type(), current_line)
                current_line = self.term.print_line(" How unlucky... You're imprisonned...", current_line)
                self.game_board.cases()[player.position()].imprison(player)

            ## Cas Chance ##
            elif (self.game_board.cases()[player.position()].type() == "Luck"):
                current_line = self.term.print_line(" You're now on - " +  self.game_board.cases()[player.position()].type(), current_line)
                self.game_board.cases()[player.position()].action(player)

            ## Cas Taxes ##
            elif (self.game_board.cases()[player.position()].type() == "Taxes"):
                current_line = self.term.print_line(" You're now on - " +  self.game_board.cases()[player.position()].type(), current_line)
                current_line = self.term.print_line(" Oh nooooo, you have to pay taxes... It costs " +
                      str(self.game_board.cases()[player.position()].value()) + "k€" , current_line)
                self.game_board.cases()[player.position()].pay(player)

            ## Cas Compagnies, Gares et Propriétés ##
            if (self.game_board.cases()[player.position()].type() in ["Company", "Train Station", "Property"]):
                current_line = self.term.print_line(" You're now on - " +  self.game_board.cases()[player.position()].type(), current_line)
                if (self.game_board.is_owned(player.position()) == player.id()):
                    current_line = self.term.print_line(" Welcome Home !!!",current_line)
                elif self.game_board.is_owned(player.position()) is not None:
                    id_of_owner = self.game_board.is_owned(player.position())
                    current_line = self.term.print_line(" You must pay a tax to player " + str(id_of_owner), current_line)

                    ## Cas Companie ##
                    if (self.game_board.cases()[player.position()].type() == "Company"):
                        if (self.game_board.is_owned(12) == self.game_board.is_owned(28)):
                            current_line = self.term.print_line(" The rent is 10 times the sum of the value on the dices", current_line)
                            self.game_board.transaction(player, self.players[id_of_owner], 12 * dice_result)
                        else:
                            current_line = self.term.print_line(" The rent is 4 times the sum of the value on the dices", current_line)
                            self.game_board.transaction(player, self.players[id_of_owner], 4 * dice_result)

                    ## Cas Gare ##
                    elif (self.game_board.cases()[player.position()].type() == "Train Station"):
                        nb_train_stations_owned = 0
                        for i in range(5, 36, 10):
                            if (self.game_board.is_owned(i) == id_of_owner):
                                nb_train_stations_owned += 1
                        current_line = self.term.print_line(" It costs " + str(self.game_board.cases()[player.position()].rent(nb_train_stations_owned)) +
                              "k€", current_line)
                        self.game_board.transaction(player, self.players[id_of_owner],
                                                    self.game_board.cases()[player.position()].rent(
                                                        nb_train_stations_owned))

                    ## Cas Propriété ##
                    else:
                        current_line = self.term.print_line(" It costs " + str(self.game_board.cases()[player.position()].rent()) + "k€", current_line)
                        self.game_board.transaction(player, self.players[id_of_owner],
                                                    self.game_board.cases()[player.position()].rent())
                else:
                    current_line = self.term.print_line(" Free space ", current_line)
                    self.game_board.cases()[player.position()].show_case(10,10, self.screen)
                    current_line = self.term.print_line(" It costs " + str(self.game_board.cases()[player.position()].value()) + "k€", current_line)
                    if (self.game_board.cases()[player.position()].value() > player.money()):
                        current_line = self.term.print_line(" You don't have enough money to buy the property",current_line, color=rouge)
                    else:
                        current_line = self.term.print_line(" You can buy the property ", current_line, color=vert)
                        current_line = self.term.print_line(" Do you want to buy it ?", current_line)
                        current_line = self.term.print_line(" A - Yes", current_line)
                        current_line = self.term.print_line(" B - No", current_line)
                        output = self.term.print_input(current_line, lambda input: input == "A" or input == "B")
                        current_line += 1
                        if output == "A":
                            self.game_board.buy_property(player)
                        else:
                            pass


        while (player.money() < 0 and len(property_player) > 0):
            current_line = self.term.print_line(
                "You don't have enough money, you have to sell some houses or some properties",current_line)
            current_line = self.term.print_line("Here are your properties :", current_line)
            self.display_properties(property_player)
            current_line = self.term.print_line(
                "Do you want to sell a house or a property to the bank ?",current_line)
            current_line = self.term.print_line("A - House",current_line)
            current_line = self.term.print_line("B - Property", current_line)
            output = self.term.print_input(current_line, lambda input: input == "A" or input == "B")
            current_line += 1
            if (output == "A"):
                current_line = self.term.print_line("On which property do you want to sell a house ? Enter the id diplayed in the recap :", current_line)
                def f(input):
                    for i in range(1,len(property_player)):
                        if input == str(i):
                            return True
                    return False
                id_property = self.term.print_input(current_line, f)
                current_line+=1
                if (self.game_board.cases()[property_player[id_property - 1].id()].nb_houses() == 0):
                    current_line = self.term.print_line("You don't have any house on this property",current_line)
                else:
                    price_house = self.game_board.cases()[
                        property_player[id_property - 1].id()].price_houses()
                    former_nb_houses = self.game_board.cases()[
                        property_player[id_property - 1].id()].nb_houses()
                    self.game_board.cases()[property_player[id_property - 1].id()].set_nb_houses(
                        former_nb_houses - 1)
                    player.set_money(player.money() + price_house)
                    current_line = self.term.print_line(" You earned " + str(price_house) + "k€", current_line)
            elif (output == "B"):
                current_line = self.term.print_line("Which property ? Enter the id diplayed above :", current_line)
                def f(input):
                    for i in range(1, len(property_player)):
                        if input == str(i):
                            return True
                    return False
                id_property = self.term.print_input(current_line, f)
                current_line +=1
                self.game_board.sell_property(player, property_player[id_property - 1].id())

        if (player.money() < 0):
            print(" \n \n You've lost the game \n \n")

        print("\n \n Here is a brief recap of your situation : \n \n")
        print("██████████████████████████████████████████")
        print("\n Your Bank account : ", player.money(), " € \n \n")
        print(" Properties : \n")
        property_player = self.game_board.list_property(player)
        self.display_properties(property_player)
        print("██████████████████████████████████████████")

        if (len(property_player) > 0):

            ## Actions joueur ##
            answer = ""
            while (answer != 6):
                print("\n \n Select the action you want to make : \n \n"
                      " 1 - Display information about one of your properties (Does not work for train stations or companies \n \n"
                      " 2 - Build a house \n \n"
                      " 3 - Sell a house \n \n"
                      " 4 - Display information about the properties of another player \n \n"
                      " 5 - Make an offer to another player \n \n"
                      " 6 - End your turn \n \n")
                answer = int(input(""))

                ## Affichage informations ##
                if (answer == 1):
                    self.display_properties(property_player)
                    print(
                        " \n Which property do you want the information to be displayed ? Enter the id diplayed above : \n \n")
                    id_property = int(input(""))
                    if (id_property < 1 or id_property > len(property_player) or property_player[
                        id_property - 1].type() != "Property"):
                        print(" The number you entered is invalid")
                    else:
                        property_player[id_property - 1].print_information()

                ## Construction maison ##
                elif (answer == 2):
                    self.display_properties(property_player)
                    print(" \n On which property do you want to build a house ? Enter the id diplayed above : \n \n")
                    id_property = int(input(""))
                    if (id_property < 1 or id_property > len(property_player) or property_player[
                        id_property - 1].type() != "Property"):
                        print("\n The number you entered is invalid")
                    else:
                        ids_monopole = self.game_board.ids_same_monopole(property_player[id_property - 1].monopole_id())
                        size_monopole = len(ids_monopole)
                        if (size_monopole == 2):
                            if (self.game_board.is_owned(ids_monopole[0]) == self.game_board.is_owned(ids_monopole[1])):
                                price_house = self.game_board.cases()[
                                    property_player[id_property - 1].id()].price_houses()
                                if (player.money() < price_house):
                                    print("\n You don't have enough money to build a house \n")
                                else:
                                    former_nb_houses = self.game_board.cases()[
                                        property_player[id_property - 1].id()].nb_houses()
                                    self.game_board.cases()[property_player[id_property - 1].id()].set_nb_houses(
                                        former_nb_houses + 1)
                                    player.set_money(player.money() - price_house)
                                    print(" \n \n You've builed a house on ",
                                          self.game_board.cases()[property_player[id_property - 1].id()].name())

                            else:
                                print(" \n You have to own the whole monopole to build a house. \n")
                        else:
                            if (self.game_board.is_owned(ids_monopole[0]) == self.game_board.is_owned(
                                    ids_monopole[1]) and self.game_board.is_owned(
                                ids_monopole[1]) == self.game_board.is_owned(ids_monopole[2])):
                                price_house = self.game_board.cases()[
                                    property_player[id_property - 1].id()].price_houses()
                                if (player.money() < price_house):
                                    print("\n You don't have enough money to build a house \n")
                                else:
                                    former_nb_houses = self.game_board.cases()[
                                        property_player[id_property - 1].id()].nb_houses()
                                    self.game_board.cases()[property_player[id_property - 1].id()].set_nb_houses(
                                        former_nb_houses + 1)
                                    player.set_money(player.money() - price_house)
                                    print(" \n \n You've builed a house on ",
                                          self.game_board.cases()[property_player[id_property - 1].id()].name())
                            else:
                                print(" \n You have to own the whole monopole to build a house. \n")

                ## Vente maison ##
                elif (answer == 3):
                    print(
                        " \n On which property do you want to sell a house ? Enter the id diplayed in the recap : \n \n")
                    id_property = int(input(""))
                    if (id_property < 1 or id_property > len(property_player) or property_player[
                        id_property - 1].type() != "Property"):
                        print("\n The number you entered is invalid")
                    else:
                        if (self.game_board.cases()[property_player[id_property - 1].id()].nb_houses() == 0):
                            print("\n You don't have any house on this property. \n \n")
                        else:
                            price_house = self.game_board.cases()[
                                property_player[id_property - 1].id()].price_houses()
                            former_nb_houses = self.game_board.cases()[
                                property_player[id_property - 1].id()].nb_houses()
                            self.game_board.cases()[property_player[id_property - 1].id()].set_nb_houses(
                                former_nb_houses - 1)
                            player.set_money(player.money() + price_house)
                            print(" You earned ", price_house, "€ \n \n")

                ## Affichage informations propriétés autre joueur ##
                elif (answer == 4):
                    print("\n Write the name of the player whose property you want to see : \n \n")
                    player_name = input("")
                    id_player = self.find_player(player_name)
                    if (id_player == 0):
                        print("\n The player you entered does not exist. \n \n")
                    else:
                        seller_properties = self.game_board.list_property(self.players[id_player])
                        if (len(seller_properties) == 0):
                            print("\n This player you chose does not have any property. \n \n")
                        else:
                            self.display_properties(seller_properties)
                            answer2 = ""
                            while (answer2 != "B"):
                                print(
                                    "\n \n Do you want to display information about one of those properties ? (Does not work for train stations or companies) \n A- Yes \n B- No")
                                answer2 = input("")
                                if answer2 == "A":
                                    print(" \n Which property ? Enter the id diplayed before : \n \n")
                                    id_property = int(input(""))
                                    if (id_property < 1 or id_property > len(seller_properties) or seller_properties[
                                        id_property - 1].type() != "Property"):
                                        print("\n The number you entered is invalid")
                                    else:
                                        seller_properties[id_property - 1].print_information()
                elif (answer == 5):
                    print("\n Write the name of the player to whome you want to make an offer : \n \n")
                    player_name = input("")
                    id_seller = self.find_player(player_name)
                    if (id_seller == 0):
                        print("\n The player you entered does not exist. \n \n")
                    else:
                        seller_properties = self.game_board.list_property(self.players[id_seller])
                        if (len(seller_properties) == 0):
                            print("\n This player you chose does not have any property. \n \n")
                        else:
                            self.display_properties(seller_properties)
                            print(
                                "\n \n Which property belonging to the other player do you want ? Enter the id diplayed above : \n \n")
                            id_seller_property = int(input(""))
                            if (id_seller_property < 1 or id_seller_property > len(seller_properties)):
                                print("\n The number you entered is invalid")
                            elif (self.game_board.houses_on_monopole(
                                    seller_properties[id_seller_property - 1].id()) > 0):
                                print("\n \n You can't buy a house in a monopole where some houses are built \n \n")
                            else:
                                self.display_properties(property_player)
                                print(
                                    "\n \n Which property do you offer ? Enter the id diplayed above : \n \n")
                                id_buyer_property = int(input(""))
                                if (id_buyer_property < 1 or id_buyer_property > len(property_player)):
                                    print("\n The number you entered is invalid \n \n")
                                elif (self.game_board.houses_on_monopole(
                                        property_player[id_seller_property - 1].id()) > 0):
                                    print(
                                        "\n \n You can't sell a house in a monopole where some houses are built \n \n")
                                else:
                                    print("\n How much do you offer for the exchange ? \n \n")
                                    price_offer = int(input(""))
                                    if (player.money() < price_offer):
                                        print(" \n \n You don't have enough money to make such an offer \n \n")
                                    else:
                                        print(
                                            "\n \n ", self.players[id_seller].name(),
                                            ", do you accept to exchange ",
                                            seller_properties[id_seller_property - 1].name(), " with ",
                                            property_player[id_buyer_property - 1].name(), " for ", price_offer,
                                            " € ? \n A- Yes \n B- No")
                                        answer2 = input("")
                                        if (answer2 == "A"):
                                            self.exchange_properties(player.id(), id_seller, price_offer,
                                                                     property_player[id_buyer_property - 1].id(),
                                                                     seller_properties[id_seller_property - 1].id())
                                            property_player = self.game_board.list_property(player)
                                            print(" \n \n The exchange took place ! \n \n")
                                        elif (answer2 == "B"):
                                            print("\n \n The offer was refused. \n \n")
                                        else:
                                            print(" \n \n You entered an incorrect answer \n \n")
                elif (answer == 6):
                    pass
                else:
                    print(" You entered an incorrect answer \n \n")

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
    game = Game_graphical()
    game_var = game.begin_game()
    nb_players = len(game_var) - 1
    new_game = Game_graph(True, nb_players)
    nb_players_in_game = nb_players
    id_current_player = random.randint(1, nb_players)
    while (nb_players_in_game > 1):
        if (id_current_player > nb_players):
            id_current_player = 1
        if (new_game.players[id_current_player].money() > 0):
            new_game.player_tour(new_game.players[id_current_player], new_game)
            if (new_game.players[id_current_player].money() < 0):
                nb_players_in_game -= 1
        id_current_player += 1
    new_game.end_game(True)