import rpn
from pytest import approx
def test_edge_cases():
    #edge cases
    assert rpn.evaluate("5") == approx(5.0) 
    assert rpn.evaluate("2.0") == approx(2.0)
    assert rpn.evaluate("-1") == approx(-1.0)
    assert rpn.evaluate("11") == approx(11.0)

#Happy path cases
def test_happy_cases():
    assert rpn.evaluate("4 5 +") == approx(9.0) 
    assert rpn.evaluate("5 2 -") == approx(3.0)
    assert rpn.evaluate("2 8 *") == approx(16.0)
    assert rpn.evaluate("14 2 %") == approx(7.0)
    assert rpn.evaluate("1 2 3 + -")== approx(-4.0)
    assert rpn.evaluate("4 3 * 5 -")== approx(7.0)