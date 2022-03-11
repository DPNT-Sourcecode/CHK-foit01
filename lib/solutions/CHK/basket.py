


class Basket:
    """
    Our price table and offers: 
    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    +------+-------+------------------------+
    """

    def __init__(self, products, promotions):
        self.products = products
        self.promotions = promotions


    @property
    def get_total_price(self):
        return sum([p.quantity * p.price for p in self.products])

