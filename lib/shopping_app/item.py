
class Item():

    from ownable import set_owner

    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Cuando se crea una instancia de Elemento, la instancia de Elemento (yo) se almacena en una variable de clase llamada instancias.
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # Devolver instancias ==> Item.item_all() devuelve todas las instancias de Item que se han generado hasta ahora.
        return Item.instances
