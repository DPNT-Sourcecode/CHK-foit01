

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_price = 0
    basket = {e: skus.count(e) for e in set(skus)}
    prices = {
        'A': {'price': 50, 'special_offer': [3, 130]},
        'B': {'price': 30, 'special_offer': [2, 45]},
        'C': {'price': 20},
        'D': {'price': 15}

    }
    for item, amount in basket.items():
        try:
            special_offer = prices[item]['special_offer']
            has_special_offer = amount >= special_offer[0]
            
            special_offer_amounts = (int(amount/special_offer[0]), amount%special_offer[0])
            price = prices[item]['price'] if has_special_offer else 0
        except KeyError:
            # Noe special offers available
            pass
        total_price += prices[item]['price'] * amount
    return total_price

    


