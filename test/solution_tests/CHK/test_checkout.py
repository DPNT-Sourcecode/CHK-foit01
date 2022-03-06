from lib.solutions.CHK import checkout_solution

def test_checkout_solution():
    assert checkout_solution.checkout('AAB') == {'A': 2, 'B':1}