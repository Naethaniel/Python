def checkio(number: int) -> int:
    number = str(number)
    output = 1
    for letter in number:
        if letter != '0':
            output *= int(letter)
    return output

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
