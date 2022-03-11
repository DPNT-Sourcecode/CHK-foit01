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

    def __str__(self):
        return f'{self.name} (£{self.price})'

    def __repr__(self):
        return f'{self.name} (£{self.price})'

    def reduce_quantity(self, quantity):
        self.quantity -= quantity