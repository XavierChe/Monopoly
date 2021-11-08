class Player:
    id : int
    money : int
    position : int
    
    def __init__(self, id_num = 0, money = 0, position = 0):
        self.id = id_num
        self.money = money
        self.position = position