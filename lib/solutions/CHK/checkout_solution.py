

# noinspection PyUnusedLocal
# skus = unicode string
from .product import create_products

def checkout(skus):

    products = create_products(skus)
    print(products)
    
    return 0

    



