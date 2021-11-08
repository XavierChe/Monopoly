class Player:
    _id : int
    _money : int
    _position : int
    
    def __init__(self, id_num = 0, money = 10000, position = 0):
        self._id = id_num
        self._money = money
        self._position = position

    def position(self):
        return self._position

    def id(self):
        return self._id

    def money(self):
        return self._money

    def set_money(self, money):
        self._money=money

    def set_position(self, pos):
        self._position=pos