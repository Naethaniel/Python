def checkio(n, m):
    first = bin(n)
    second = bin(m)

    if len(first) > len(second):
        diff = len(first) - len(second)
        second = list(second)
        for i in range(diff):
            second.insert(2, '0')
        second = ''.join(second)
    if len(first) < len(second):
        diff = len(second) - len(first)
        first = list(first)
        for i in range(diff):
            first.insert(2, '0')
        first = ''.join(first)

    # calculate diff
    diff = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            diff += 1
    return diff


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"

print(checkio(117, 17))