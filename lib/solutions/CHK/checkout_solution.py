

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_price = 0
    basket = {e: skus.count(e) for e in set(skus)}
    prices = {
        'A': {'price': 50, 'special_offer': [3, 130]},
        'B': {'price': 30, 'special_offer': [2, 45]},
        'C': {'price': 20},
        'D': {'price': 15},
        'E': {'price': 40}, 'special_offer': []

    }
    for item, amount in basket.items():
        try:
            special_offer = prices[item].get('special_offer', None)
        except KeyError:
            # Item not in the price table an offers
            return -1
        has_special_offer = True if special_offer else False

        if has_special_offer:           
            special_offer_amounts = (
                int(amount/special_offer[0]),
                amount%special_offer[0]
            ) 
            special_offer_price = (special_offer_amounts[0] * special_offer[1]) + (special_offer_amounts[1] * prices[item]['price'])

        total_price += prices[item]['price'] * amount if not has_special_offer else special_offer_price

    return total_price

    




