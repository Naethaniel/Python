from typing import List
from math import acos, degrees


def checkio(a: int, b: int, c: int) -> List[int]:
    if (a + b) < c or (a + c) < b or (b + c) < a:
        return [0, 0, 0]

    cos_a = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    cos_b = (c ** 2 + a ** 2 - b ** 2) / (2 * c * a)

    a = round(degrees(acos(cos_a)))
    b = round(degrees(acos(cos_b)))

    if a == 0 or b == 0:
        return [0, 0, 0]

    c = 180 - a - b

    output = [a, b, c]
    output.sort()
    return output


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(8, 6, 7))

    print(checkio(11, 20, 30))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
