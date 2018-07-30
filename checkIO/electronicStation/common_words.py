def checkio(first, second):
    common = []
    first = first.split(',')
    second = second.split(',')
    if len(first) < len(second):
        first, second = second, first

    for elem in first:
        if elem in second:
            common.append(elem)
    common.sort()
    return ','.join(common)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
