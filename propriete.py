from player import Player
import random
import pygame
import pygame.locals as pl
pygame.init()

class Case:
    _type: str
    _id: int

    def __init__(self,type="#",id=0):
        self._type = type
        self._id = id

    # === Accesseurs ===
    
    def id(self):
        return self._id

    def type(self):
        return self._type


class Property(Case):
    _name: str
    _id: int #Possiblement osef
    # Prix achat
    _value: int
    _owner: int
    _nb_houses: int
    _price_houses: int
    #Prix à payer si pas proprio
    _rent: list

    def __init__(self,name="#",id=0, monopole_id=0, value=0,owner=0,nb_houses=0,price_houses=0,rent=[0]*6):
        super().__init__("Property",id)
        self._name = name.replace("_"," ")
        self._monopole_id = monopole_id
        self._value = value
        self._owner = owner
        self._nb_houses = nb_houses
        self._price_houses = price_houses
        self._rent = rent
        
    # ===   Accesseurs   ===
    def name(self):
        return self._name
    
    def monopole_id(self):
        return self._monopole_id

    def value(self):
        return self._value

    def owner(self):
        return self._owner

    def nb_houses(self):
        return self._nb_houses

    def price_houses(self):
        return self._price_houses

    def rent(self):
        return self._rent[self._nb_houses]

    def set_owner(self,id):
        self._owner=id

    def set_nb_houses(self,n):
        self._nb_houses=n

    def print_information(self):
        print("\n Name of the property : ", self._name)
        print("\n Price of a house : ",self._price_houses)
        print("\n Number of houses : ", self._nb_houses)
        for i in range(5):
            print("\n Price of the rent with : ", i, "houses : ", self._rent[i])
        print("\n Price of the rent with a hotel : ", self._rent[5])


class Luck(Case):
    def __init__(self,id):
        super().__init__("Luck",id)

    def action(self, p : Player):
        n = random.randint(1,8)
        if (n==1):
            print(" Allez en prison. Allez tout droit à la prison. Ne passez pas par la case départ, ne reçevez pas 200€.\n")
            p.set_free(False)
            p.set_position(10)
        if (n==2):
            print(" Rendez-vous Rue de La Paix. Si vous passez par la case départ, recevez 200€.\n")
            if (p.position()>39):
                p.set_money(p.money()+200)
            p.set_position(39)
        if (n==3):
            print(" Rendez-vous Avenue Henri Martin. Si vous passez par la case départ, recevez 200€.\n")
            if(p.position()>24):
                p.set_money(p.money()+200)
            p.set_position(24)
        if (n==4):
            print(" Rendez-vous case Départ. Recevez 400€.\n")
            p.set_position(0)
            p.set_money(p.money()+400)
        if (n == 5):
            print(" La banque vous verse un dividende de 50€.\n")
            p.set_money(p.money()+50)
        if (n == 6):
            print(" Vous êtes libéré de prison. Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.\n")
            p.set_escape_card(p.escape_card()+1)
        if (n == 7):
            print(" Amende pour excès de vitesse. Payez 50€.\n")
            p.set_money(p.money()-50)
        if (n == 8):
            print(" Amende pour ivresse. Payez 50€.\n")
            p.set_money(p.money()-50)

class GoToPrison(Case):
    def __init__(self):
        super().__init__("Go to Prison",30)

    def imprison(self,player : Player):
        player.set_position(10)
        player.set_free(False)

class Prison(Case):
    def __init__(self):
        super().__init__("Prison",10)

    def exit_prison(self,player : Player):
        player.set_free(True)
        player.set_money(player.money()-50)
        player.set_round_in_prison(0)
        return True

    def rounds_passed(self,player : Player):
        if (player.round_in_prison()==3):
            print(" You can exit the prison !\n")
            return self.exit_prison(player)
        else :
            print(" You can't exit the prison...\n")
            player.set_round_in_prison(player.round_in_prison()+1)
            return False

    def trying_to_escape_prison(self, dice_1, dice_2, player: Player):
        if (dice_1==dice_2):
            print(" You can exit the prison ! But you have to pay 50€.\n")
            return self.exit_prison(player)
        else:
            return self.rounds_passed(player)

class Taxes(Case):
    def __init__(self, id=0, value=0):
        super().__init__("Taxes", id)
        self._value_tax = value

    def value(self):
        return self._value_tax

    def pay(self, player: Player):
        player.set_money(player.money()-self._value_tax)

class Company(Case):
    def __init__(self, id, name="#", owner=0):
        super().__init__("Company", id)
        self._value=100
        self._name=name
        self._owner=owner

    def value(self):
        return self._value

    def name(self):
        return self._name

    def owner(self):
        return self._owner

    def set_owner(self, id):
        self._owner = id

class TrainStation(Case):
    def __init__(self, name="#", id=0):
        super().__init__("Train Station", id)
        self._name = name
        self._value = 200
        self._owner = 0
        # On n'appellera jamais la case 0 de rent, on appellera la case en fonction du nombre de gares possédées par le joueur
        self._rent = [0,25,50,100,200]

    def name(self):
        return self._name

    def value(self):
        return self._value

    def owner(self):
        return self._owner

    def rent(self,i):
        return self._rent[i]

    def set_owner(self,id):
        self._owner=id