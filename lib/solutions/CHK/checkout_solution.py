

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
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

def checkout(skus):
    

    return 0

    


