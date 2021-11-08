class Property:
    name: str
    id: int
    value: int
    owner: str
    nb_houses: int
    price_houses: int

    def __init__(self):
        self.name = "#"
        self.id = 0
        self.value = 0
        self.owner = "#"
        self.nb_houses = 0
        self.price_houses = 0

    def __str__(self):
        prop = ""
        prop += "+---------------+\n"  # 17 elements
        prop += "|               |\n"
        prop += "+---------------+\n"
        for i in range(10) :
            prop += "|               |\n"
        prop += "+---------------+\n"
        return prop

a = Property()
print(a)
