from player import Player
import random


class Luck:
    def __init__(self):
        pass
    def type(self):
        return "Luck"
    def action(self, p : Player):
        n = random.randint(1,10)
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