


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
        return sum([p.quantity * p.price for p in self.products]) - self.calculate_discounts

    def calculate_free(self):
        for f_prom in [p for p in self.promotions if p.type == 'free']:
            for prod in self.products:


    @property
    def calculate_discounts(self):
        total_discount = 0

        for prom in self.promotions:
            for prod in self.products:
                if prom.qualifying_product == prod.name:
                    num_promotions = prod.quantity // prom.qualifying_qty
                    
                    elif prom.type == 'free':
                        total_qty_reduce
        return total_discount
                    
                    


