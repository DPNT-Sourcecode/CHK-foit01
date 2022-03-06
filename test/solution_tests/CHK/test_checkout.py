from lib.solutions.CHK import checkout_solution

def test_checkout_solution():
    assert checkout_solution.checkout('AAB') == 130
    assert checkout_solution.checkout('BBBB') == 90
    assert checkout_solution.checkout('CCCCAAABB') == 255
    assert checkout_solution.checkout('XXXX') == -1