

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = {e:skus.count(e) for e in set(skus)}
    return 'hello'

