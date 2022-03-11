

# noinspection PyUnusedLocal
# skus = unicode string
from .product import create_products
from .promotion import create_promotions
from .basket import Basket

def checkout(skus):

    try:
        products = create_products(skus)
    except KeyError:
        return -1
    promotions = create_promotions()

    basket = Basket(products, promotions)
    print(products)
    
    return basket.get_total_price

    

