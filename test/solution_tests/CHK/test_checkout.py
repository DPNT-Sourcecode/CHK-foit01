from lib.solutions.CHK import checkout_solution

def test_checkout_solution():
    assert checkout_solution.checkout('AAB') == 130
    assert checkout_solution.checkout('CCCCAAABB') == 255
    assert checkout_solution.checkout('XXXX') == -1
    assert checkout_solution.checkout('AAAAAAAA') == 330
    assert checkout_solution.checkout('AAAAAAAAA') == 400
    assert checkout_solution.checkout('BBBCCEE') == 165
    assert checkout_solution.checkout('BAECDAACDE') == 280
    assert checkout_solution.checkout('EEEEBB') == 160

