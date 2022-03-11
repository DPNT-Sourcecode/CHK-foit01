


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

    def reduce_product_quantity(self, product, qty):
        for p in self.products:
            if product.name == p.name:
                p.reduce_quantity()

    def calculate_free(self):
        for f_prom in [p for p in self.promotions if p.type == 'free']:
            for prod in self.products:
                num_promotions = prod.quantity // f_prom.qualifying_qty
                reduce_number = num_promotions * f_prom.discount_qty
                self.reduce_product_quantity(prod, reduce_number)

    @property
    def calculate_discounts(self):
        total_discount = 0

        for c_prom in [p for p in self.promotions if p.type == 'cumulative']:
            for prod in self.products:
                if c_prom.qualifying_product == prod.name:
                    num_promotions = prod.quantity // c_prom.qualifying_qty
                    total_discount += num_promotions * c_prom.discount_qty
        print(f'total discount {total_discount}')
        return total_discount
                    
                    
