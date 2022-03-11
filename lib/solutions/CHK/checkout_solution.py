

# noinspection PyUnusedLocal
# skus = unicode string
from .product import create_products

def checkout(skus):

    products = create_products(skus)
    
    create_products(skus)
    return 0

    



