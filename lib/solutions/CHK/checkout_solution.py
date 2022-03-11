

# noinspection PyUnusedLocal
# skus = unicode string
from .product import create_products
from .promotion import create_promotions

def checkout(skus):

    products = create_products(skus)
    promotions = create_promotions()
    print(products)
    
    return 0

    

