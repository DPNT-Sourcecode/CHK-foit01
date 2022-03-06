

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = {e: skus.count(e) for e in set(skus)}
    prices = {
        'A': {'price': 50, 'special_offer': [3, 130]},
        'B': {'price': 30, 'special_offer': [2, 45]},
        'C': {'price': 20},
        'D': {'price': 15}

    }
    return basket

