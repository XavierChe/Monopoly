class Property:
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
        self._name = name
        self._id = id #Probablement inutile (comme moi)
        self._value = value
        self._owner = owner
        self._nb_houses = nb_houses
        self._price_houses = price_houses
        self._rent = rent

    # ===   Accesseurs   ===
    def id(self):
        return self._id

    def name(self):
        return self._name

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


    # ===   Méthodes   ===


