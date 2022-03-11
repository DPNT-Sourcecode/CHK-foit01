PRODUCTS = {
    'A': {'name': 'A', 'price': 50},
    'B': {'name': 'B', 'price': 30},
    'C': {'name': 'C', 'price': 20},
    'D': {'name': 'D', 'price': 15},
    'E': {'name': 'E', 'price': 40},
}


def create_products(skus: str) ->  list:
    count = {s: skus.count(s) for s in set(skus)}
    print(count)



class Product:

    def __init__(self, name, quantity):
        self.name = PRODUCTS[name]['name']
        self.price = PRODUCTS[name]['price']
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} (£{self.price}'

