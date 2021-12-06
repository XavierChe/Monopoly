class Player:
    _id : int
    _money : int
    _position : int
    
    def __init__(self, id_num=0, money=200, position=0,free=True,escape=0):
        self._id = id_num
        self._money = money
        self._position = position
        self._free=free
        self._escape_card=escape
        
    def position(self):
        return self._position

    def id(self):
        return self._id

    def money(self):
        return self._money

    def free(self):
        return self._free

    def escape_card(self):
        return self._escape_card

    def set_money(self, money):
        self._money=money

    def set_position(self, pos):
        self._position=pos

    def set_free(self,b):
        self._free=b

    def set_escape_card(self,c):
        self._escape_card=c
