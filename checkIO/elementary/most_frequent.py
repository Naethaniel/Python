def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    dict = {}
    if len(data) == 1:
        return data[0]
    for elem in data:
        if elem in dict.keys():
            dict[elem] += 1
        else:
            dict[elem] = 0
    best = 0
    res = ''
    for elem in dict:
        if dict[elem] > best:
            res = elem
            best = dict[elem]
    return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')

print(most_frequent(["a"]))
