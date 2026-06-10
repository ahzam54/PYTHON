from Calculator import square


# after installing pytest
# using pytest in terminal to test the test code .
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16

def test_zero():
    assert square(0) == 0
    