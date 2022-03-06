

# noinspection PyUnusedLocal
# skus = unicode string
def sort_inside_value(elem):
    return elem['offer'][0]

def checkout(skus):
    total_price = 0
    basket = {e: skus.count(e) for e in set(skus)}
    print()
    print('basket', basket)
    prices = {
        'A': {
            'price': 50,
            'special_offer': [
                {
                    "type" : "cumulative",
                    "offer": [3, 130]
                },
                {
                    "type" : "cumulative",
                    "offer": [5, 200]
                }                
            ]
                
            
        },
        'B': {
            'price': 30,
            'special_offer': [
                {
                    "type" : "cumulative",
                    "offer": [2, 45]
                }              
            ]
        },
        'C': {
            'price': 20
        },
        'D': {
            'price': 15
        },
        'E': {
            'price': 40,
            'special_offer': [
                {
                    "type" : "free",
                    "offer": [2, 'B']
                }              
            ]
        }
    }
    for item, amount in basket.items():

        print(f'item: {item}, amount: {amount}')
        special_offer = None
        try:
            if prices[item].get('special_offer', None):
                for offer in sorted(prices[item].get('special_offer', None), key=sort_inside_value, reverse=True):
                    if amount >= offer["offer"][0]:
                        special_offer = offer
                        break
        except KeyError:
            # Item not in the price table an offers
            return -1
        print(f'special_offer: {special_offer}')
        has_special_offer = True if special_offer else False
        print(f'has_special_offer: {has_special_offer}')

        if has_special_offer:           
            special_offer_amounts = (
                int(amount/special_offer['offer'][0]),
                amount%special_offer['offer'][0]
            ) 
            special_offer_price = (special_offer_amounts[0] * special_offer['offer'][1]) \
                + (special_offer_amounts[1] * prices[item]['price'])
        price = prices[item]['price'] * amount if not has_special_offer else special_offer_price
        print('price', price)
        total_price += price

    return total_price

    





