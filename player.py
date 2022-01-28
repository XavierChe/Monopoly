#import pygame

#pygame.init()

#position_possible = [(21*height//22, 21*height//22),(19*height//22, 21*height//22),(17*height//22, 21*height//22),(15*height//22, 21*height//22),(13*height//22, 21*height//22),(11*height//22, 21*height//22),(9*height//22, 21*height//22),(7*height//22, 21*height//22),(5*height//22, 21*height//22),(3*height//22, 21*height//22),(height//22, 21*height//22),(height//22, 19*height//22),(height//22, 17*height//22),(height//22, 15*height//22),(height//22, 13*height//22),(height//22, 11*height//22),(height//22, 9*height//22),(height//22, 7*height//22),(height//22, 5*height//22),(height//22, 3*height//22),(height//22, height//22),(3*height//22, height//22),(5*height//22, height//22),(7*height//22, height//22),(9*height//22, height//22),(11*height//22, height//22),(13*height//22, height//22),(15*height//22, height//22),(17*height//22, height//22),(19*height//22, height//22),(21*height//22, height//22),(21*height//22, 3*height//22),(21*height//22, 5*height//22),(21*height//22, 7*height//22),(21*height//22, 9*height//22),(21*height//22, 11*height//22),(21*height//22, 13*height//22),(21*height//22, 15*height//22),(21*height//22, 17*height//22),(21*height//22, 19*height//22)]

class Player:
    _id : int
    _money : int
    _position : int
    _free : bool
    _escape_card : int
    _round_in_prison : int
    _player_name : str
    
    def __init__(self, id_num=0, player_name="#", money=1500, position=0,free=True,escape=0,round_in_prison=0):
        self._id = id_num
        self._player_name=player_name
        self._money = money
        self._position = position
        self._free=free
        self._escape_card=escape
        self._round_in_prison=round_in_prison
        
    def position(self):
        return self._position

    def id(self):
        return self._id

    def name(self):
        return self._player_name

    def money(self):
        return self._money

    def free(self):
        return self._free

    def escape_card(self):
        return self._escape_card

    def round_in_prison(self):
        return self._round_in_prison

    def set_money(self, money):
        self._money=money

    def set_position(self, pos):
        self._position=pos

    def set_free(self,b):
        self._free=b

    def set_escape_card(self,c):
        self._escape_card=c

    def set_round_in_prison(self,c):
        self._round_in_prison=c

    def show_player(self):
        if self.id() == 1:
            pion1 = pygame.image.load('pictures/PION1.png')
            pion1_width, pion1_height = pion1.get_size()
            screen.blit(pion1,
                        (position_possible[self.position()][0] - pion1_width // 2, position_possible[self.position()][1] - pion1_height // 2))