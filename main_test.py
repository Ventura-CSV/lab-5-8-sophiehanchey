
import main1
import main2


def test_main():
    numbers = [5, 4, 3, 2, 1]

    others = main1.myfunc(numbers)
    first, *others = main2.myfunc(numbers)
    print(others)

# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"
