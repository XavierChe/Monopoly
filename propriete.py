from player import Player
import random

class Case:
    _name: str
    _id: int

    def __init__(self,name="#",id=0):
        self._name = name
        self._id = id

    # === Accesseurs ===
    
    def id(self):
        return self._id

    def name(self):
        return self._name


class Property(Case):
    _name: str
    _id: int #Possiblement osef
    # Prix achat
    _value: int
    _owner: int
    _nb_houses: int
    _price_houses: int
    #Prix à payer si pas proprio
    _rent : int

    def __init__(self,name="#",id=0,value=0,owner=0,nb_houses=0,price_houses=0,rent=0):
        super().__init__(name,id)
        self._value = value
        self._owner = owner
        self._nb_houses = nb_houses
        self._price_houses = price_houses
        self._rent = rent

    # ===   Accesseurs   ===

    def value(self):
        return self._value

    def owner(self):
        return self._owner

    def nb_houses(self):
        return self._nb_houses

    def price_houses(self):
        return self._price_houses

    def rent(self):
        return self._rent

    def set_owner(self,id):
        self._owner=id

    def set_nb_houses(self,n):
        self._nb_houses=n

    def type(self):
        return "Property"


class Luck(Case):
    def __init__(self,id):
        super().__init__("Luck",id)

    def type(self):
        return "Luck"

    def action(self, p : Player):
        n = random.randint(1,6)
        if (n==1):
            print("Allez en prison. Allez tout droit à la prison. Ne passez pas par la case départ, ne reçevez pas 200E.")
            p.set_free(False)
        if (n==2):
            print("Rendez-vous Rue de La Paix. Si vous passez par la case départ, recevez 200E.")
            p.set_position(25)
        if (n==2):
            print("Rendez-vous Avenue Henri Martin. Si vous passez par la case départ, recevez 200E.")
            p.set_position(16)
        if (n==2):
            print("Rendez-vous case Départ. Recevez 200E.")
            p.set_position(0)
        if (n == 3):
            print("La banque vous verse un dividende de 50E.")
            p.set_money(p.money()+50)
        if (n == 4):
            print("Vous êtes libéré de prison. Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.")
            p.set_escape_card(p.escape_card()+1)
        if (n == 5):
            print("Amende pour excès de vitesse. Payez 50E.")
            p.set_money(p.money()-50)
        if (n == 6):
            print("Amende pour ivresse. Payez 50E.")
            p.set_money(p.money()-50)
        # if (n == 7):
        #     pass
        # if (n == 8):
        #     pass
        # if (n == 9):
        #     pass
        # if (n == 10):
        #     pass