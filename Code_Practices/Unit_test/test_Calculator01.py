from Calculator import square

# using pytest in terminal to test the test code .

# after installing pytest
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16
    assert square(0) == 0
    