def reverse_roman(roman_string):
    output = 0
    ROMANS = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))
    start = 0
    roman_string = list(roman_string)
    ROMANS = dict(ROMANS)
    while True:
        try:
            first = roman_string[start]
            second = roman_string[start+1]
        except IndexError:
            if start != len(roman_string):
                output += ROMANS[first]
            break
        if first + second in ROMANS:
            output += ROMANS[first+second]
            start += 2
        else:
            output += ROMANS[first]
            start += 1
    return output



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!')



