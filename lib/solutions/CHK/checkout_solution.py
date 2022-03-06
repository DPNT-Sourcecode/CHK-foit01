

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_price = 0
    basket = {e: skus.count(e) for e in set(skus)}
    print(basket)
    prices = {
        'A': {'price': 50, 'special_offer': [3, 130]},
        'B': {'price': 30, 'special_offer': [2, 45]},
        'C': {'price': 20},
        'D': {'price': 15}

    }
    for item, amount in basket.items():
        print(item, amount)
        try:
            special_offer = prices[item]['special_offer']
            has_special_offer = amount >= special_offer[0]
            
            special_offer_amounts = (int(amount/special_offer[0]), amount%special_offer[0])
            special_offer_price = (special_offer_amounts[0] * special_offer[1]) + (special_offer_amounts[1] * prices[item]['price'])

            total_price += prices[item]['price'] * amount if not has_special_offer else special_offer_price
        except KeyError:
            # No special offers available
            total_price += prices[item]['price'] * amount

    print(total_price)
    return total_price

    




