from player import Player
import random
import pygame
import pygame.locals as pl
from color import *

pygame.init()


def text_format(message, textSize, textColor):
    newFont = pygame.font.SysFont("Consolas", textSize)
    newText = newFont.render(message, True, textColor)
    return newText

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

    # Afficheur

    def show_case(self, x_init, y_init,screen):
        pygame.draw.rect(screen, white, pygame.Rect(x_init, y_init, 300, 340))
        pygame.draw.rect(screen, black, pygame.Rect(x_init + 5, y_init + 5, 290, 330), 4)
        pygame.display.flip()


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

    def __init__(self,name="#",id=0, monopole_id=0, value=0,owner=0,nb_houses=0,price_houses=0,rent=[0]*6, color =(50,50,50)):
        super().__init__("Property",id)
        self._name = name.replace("_"," ")
        self._monopole_id = monopole_id
        self._value = value
        self._owner = owner
        self._nb_houses = nb_houses
        self._price_houses = price_houses
        self._rent = rent
        self.color = color
        
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

    def show_case(self, x_init, y_init,screen):
        pygame.draw.rect(screen, white, pygame.Rect(x_init, y_init, 300, 340))
        pygame.draw.rect(screen, black, pygame.Rect(x_init + 5, y_init + 5 , 290, 330), 4)
        pygame.draw.rect(screen, self.color, pygame.Rect(x_init + 10, y_init + 10, 280, 70))
        name_prop = text_format(self.name(), 25, white)
        rec_prop = name_prop.get_rect()
        screen.blit(name_prop, (x_init + 150 - (rec_prop[2] / 2),y_init + 35))
        price_prop = text_format("k€"+str(self.value()), 30, red)
        rec_prop_price = price_prop.get_rect()
        screen.blit(price_prop, (x_init + 150 - (rec_prop_price[2] / 2), y_init + 190))
        pygame.display.flip()

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

    def show_case(self, x_init, y_init,screen):
        pygame.draw.rect(screen, white, pygame.Rect(x_init, y_init, 300, 340))
        pygame.draw.rect(screen, black, pygame.Rect(x_init + 5, y_init + 5 , 290, 330), 4)
        logo_picture = pygame.image.load('pictures/CHANCE.png')
        width_picture, height_picture = logo_picture.get_size()
        screen.blit(logo_picture, (x_init + 150 - width_picture / 2, y_init + 140 - height_picture / 2))
        name_prop = text_format("Chance", 25, black)
        rec_prop = name_prop.get_rect()
        screen.blit(name_prop, (x_init + 150 - (rec_prop[2] / 2),y_init + 20))
        pygame.display.flip()

class GoToPrison(Case):
    def __init__(self):
        super().__init__("Go to Prison",30)

    def imprison(self,player : Player):
        player.set_position(10)
        player.set_free(False)

    def show_case(self, x_init, y_init,screen):
        pygame.draw.rect(screen, white, pygame.Rect(x_init, y_init, 300, 340))
        pygame.draw.rect(screen, black, pygame.Rect(x_init + 5, y_init + 5 , 290, 330), 4)
        logo_picture = pygame.image.load('pictures/ALLER_EN_PRISON.png')
        width_picture, height_picture = logo_picture.get_size()
        screen.blit(logo_picture, (x_init + 150 - width_picture / 2, y_init + 140 - height_picture / 2))
        name_prop = text_format("Allez en Prison", 25, black)
        rec_prop = name_prop.get_rect()
        screen.blit(name_prop, (x_init + 150 - (rec_prop[2] / 2),y_init + 20))
        pygame.display.flip()

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

    def show_case(self, x_init, y_init,screen):
        pygame.draw.rect(screen, white, pygame.Rect(x_init, y_init, 300, 340))
        pygame.draw.rect(screen, black, pygame.Rect(x_init + 5, y_init + 5 , 290, 330), 4)
        logo_picture = pygame.image.load('pictures/PRISON.png')
        width_picture, height_picture = logo_picture.get_size()
        screen.blit(logo_picture, (x_init + 150 - width_picture / 2, y_init + 140 - height_picture / 2))
        name_prop = text_format("Simple Visite", 25, black)
        rec_prop = name_prop.get_rect()
        screen.blit(name_prop, (x_init + 150 - (rec_prop[2] / 2),y_init + 20))
        pygame.display.flip()

class Taxes(Case):
    def __init__(self, id=0, value=0):
        super().__init__("Taxes", id)
        self._value_tax = value

    def value(self):
        return self._value_tax

    def pay(self, player: Player):
        player.set_money(player.money()-self._value_tax)

    def show_case(self, x_init, y_init,screen):
        pygame.draw.rect(screen, white, pygame.Rect(x_init, y_init, 300, 340))
        pygame.draw.rect(screen, black, pygame.Rect(x_init + 5, y_init + 5 , 290, 330), 4)
        logo_picture = pygame.image.load('pictures/TAXE.png')
        width_picture, height_picture = logo_picture.get_size()
        screen.blit(logo_picture, (x_init + 150 - width_picture / 2, y_init + 115 - height_picture / 2))
        name_prop = text_format("Taxe de Luxe", 25, black)
        rec_prop = name_prop.get_rect()
        screen.blit(name_prop, (x_init + 150 - (rec_prop[2] / 2),y_init + 20))
        price_prop = text_format("k€"+str(self.value()), 30, red)
        rec_prop_price = price_prop.get_rect()
        screen.blit(price_prop, (x_init + 150 - (rec_prop_price[2] / 2), y_init + 190))
        pygame.display.flip()

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

    def show_case(self, x_init, y_init,screen):
        pygame.draw.rect(screen, white, pygame.Rect(x_init, y_init, 300, 340))
        pygame.draw.rect(screen, black, pygame.Rect(x_init + 5, y_init + 5 , 290, 330), 4)
        logo_picture = pygame.image.load('pictures/EAU_ELEC.png')
        width_picture, height_picture = logo_picture.get_size()
        screen.blit(logo_picture, (x_init + 150 - width_picture / 2, y_init + 120 - height_picture / 2))
        name_prop = text_format(self.name(), 25, black)
        rec_prop = name_prop.get_rect()
        screen.blit(name_prop, (x_init + 150 - (rec_prop[2] / 2),y_init + 20))
        price_prop = text_format("k€"+str(self.value()), 30, red)
        rec_prop_price = price_prop.get_rect()
        screen.blit(price_prop, (x_init + 150 - (rec_prop_price[2] / 2), y_init + 190))
        pygame.display.flip()

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

    def show_case(self, x_init, y_init,screen):
        pygame.draw.rect(screen, white, pygame.Rect(x_init, y_init, 300, 340))
        pygame.draw.rect(screen, black, pygame.Rect(x_init + 5, y_init + 5 , 290, 330), 4)
        logo_picture = pygame.image.load('pictures/GARE.png')
        width_picture, height_picture = logo_picture.get_size()
        screen.blit(logo_picture, (x_init + 150 - width_picture / 2, y_init + 115 - height_picture / 2))
        name_prop = text_format(self.name(), 25, black)
        rec_prop = name_prop.get_rect()
        screen.blit(name_prop, (x_init + 150 - (rec_prop[2] / 2),y_init + 20))
        price_prop = text_format("k€"+str(self.value()), 30, red)
        rec_prop_price = price_prop.get_rect()
        screen.blit(price_prop, (x_init + 150 - (rec_prop_price[2] / 2), y_init + 190))

        one_train_prop = text_format("1 Gare : k€"+str(self.rent(1)), 15, black)
        two_train_prop = text_format("2 Gare : k€" + str(self.rent(2)), 15, black)
        three_train_prop = text_format("3 Gare : k€" + str(self.rent(3)), 15, black)
        four_train_prop = text_format("4 Gare : k€" + str(self.rent(4)), 15, black)

        one_rec = three_train_prop.get_rect()

        screen.blit(one_train_prop, (x_init + 150 - (one_rec[2] / 2), y_init + 240))
        screen.blit(two_train_prop, (x_init + 150 - (one_rec[2] / 2), y_init + 260))
        screen.blit(three_train_prop, (x_init + 150 - (one_rec[2] / 2), y_init + 280))
        screen.blit(four_train_prop, (x_init + 150 - (one_rec[2] / 2), y_init + 300))
        pygame.display.flip()


if __name__ == "__main__":
    main_screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    T1 = Taxes()
    T2 = Prison()
    T3 = GoToPrison()
    G1 = TrainStation(name="Gare de Lyon")
    G2 = TrainStation(name="Gare Saint-Lazare")
    G3 = TrainStation(name="Gare Montparnasse")
    G4 = TrainStation(name="Gare du Nord")
    C1 = Luck(1)
    C2 = Company(1,name="Compagnie des Eaux")
    P1 = Property(color= bleu_fonce, name="Rue de la Paix")

    Go = True
    while Go:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Go = False
            if event.type == pygame.QUIT:
                Go = False
        T1.show_case(30,30,main_screen)
        T2.show_case(30, 400, main_screen)
        T3.show_case(30, 770, main_screen)
        G1.show_case(360, 30, main_screen)
        G2.show_case(360, 400, main_screen)
        G3.show_case(360, 770, main_screen)
        G4.show_case(690, 30, main_screen)
        C1.show_case(690, 400, main_screen)
        C2.show_case(690, 770, main_screen)
        P1.show_case(1020, 30, main_screen)
    pygame.quit()
