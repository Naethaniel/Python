def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    if len(line) == 0:
        return ''
    if len(line) == 1:
        return line
    output = []
    curr_longest = []

    pos = 0
    started = 1

    while True:
        letter = line[pos]
        if letter not in curr_longest:
            curr_longest.append(letter)
            pos += 1
        else:
            output.append(curr_longest)
            curr_longest = []
            pos = started
            started += 1

        if pos > len(line)-1:
            output.append(curr_longest)
            curr_longest = []
            pos = started
            started += 1

        if started+1 > len(line):
            break
    output.append(curr_longest)
    return ''.join(max(output, key=len))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')