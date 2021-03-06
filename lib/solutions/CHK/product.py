PRODUCTS = {
    'A': {'name': 'A', 'price': 50},
    'B': {'name': 'B', 'price': 30},
    'C': {'name': 'C', 'price': 20},
    'D': {'name': 'D', 'price': 15},
    'E': {'name': 'E', 'price': 40},
}


def create_products(skus: str) ->  list:
    count = {s: skus.count(s) for s in set(skus)}
    return [Product(name, qty) for (name, qty) in count.items()]



class Product:

    def __init__(self, name, quantity):
        self.name = PRODUCTS[name]['name']
        self.price = PRODUCTS[name]['price']
        self.quantity = quantity
        self.promotion = None

    def __str__(self):
        return f'{self.quantity}{self.name} (£{self.price})'

    def __repr__(self):
        return f'{self.quantity}{self.name} (£{self.price})'

    def reduce_quantity(self, quantity):
        new_qty = self.quantity - quantity
        if new_qty < 0:
            self.quantity = 0
        else:
            self.quantity = new_qty

    def apply_promotion(self, promotion):
        self.promotion = promotion

    @property
    def has_promotion(self):
        return self.promotion is not None