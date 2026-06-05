
from Calculator import square

def main():
    test_square()

def test_square():
    # if square(2) != 4:
    #     print("2 square was not 4")
    # if square(3) != 9:                    # more code
    #     print("3 square was not 9")
    # if square(4) != 16:
    #     print("4 square was not 16")

    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square was not 4")
    try:
        assert square(3) == 9
    except AssertionError:                  # more code
        print("3 square was not 9")
    try:
        assert square(4) == 16
    except AssertionError:
        print("4 square was not 16")

    # assert square(2) == 4
    # assert square(3) == 9             # less code but rise error of AssertionError
    # assert square(4) == 16

if __name__ == "__main__":
    main()

    