PROMOTIONS = [
    {
        'qualifying_product': 'A',
        'qualifying_qty': 5,
        'type': 'cumulative',
        'discount_product': 'A',
        'discount_qty': 50
    },
    {
        'qualifying_product': 'A',
        'qualifying_qty': 3,
        'type': 'cumulative',
        'discount_product': 'A',
        'discount_qty': 20
    },
    {
        'qualifying_product': 'B',
        'qualifying_qty': 2,
        'type': 'cumulative',
        'discount_product': 'AB',
        'discount_qty': 15
    },
    {
        'qualifying_product': 'E',
        'qualifying_qty': 5,
        'type': 'free',
        'discount_product': 'B',
        'discount_qty': 1
    },
]

class Promotion:
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
    def __init__(self, qualifying_product, qualifying_qty, type, discount_product, discount_qty):
        self.qualifying_product = qualifying_product
        self.qualifying_qty = qualifying_qty
        self.type = type
        self.discount_product = discount_product
        self.discount_qty = discount_qty

    def __str__(self):
        if self.type == 'free':
            return f'F Prom: {self.discount_qty}{self.discount_product} free per {self.qualifying_qty}{self.qualifying_product}'
        elif self.type == 'cumulative':
            return f'C Prom: {self.discount_qty}£ free per {self.qualifying_qty}{self.qualifying_product}'
    
    def __repr__(self):
        if self.type == 'free':
            return f'F Prom: {self.discount_qty}{self.discount_product} free per {self.qualifying_qty}{self.qualifying_product}'
        elif self.type == 'cumulative':
            return f'C Prom: {self.discount_qty}£ free per {self.qualifying_qty}{self.qualifying_product}'