def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """

    pos = 0
    di = {}
    for i in range(0, len(line), 1):
        while True:
            if pos + 1 == len(line):
                pos = 0
                break
            try:
                curr_string = line[pos:pos + i + 1]
                count = line.count(curr_string)
                if count > 1:
                    di[curr_string] = count
                pos += 1
            except IndexError:
                pos = 0
                break
    try:
        best = len(max(di, key=len))
    except ValueError:
        return 0
    return best



# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert double_substring('aaaa') == 2, "First"
#     assert double_substring('abc') == 0, "Second"
#     assert double_substring('aghtfghkofgh') == 3, "Third"
#     print('"Run" is good. How is "Check"?')

print(double_substring('aaaa'))
print(double_substring("aa"))
print(double_substring('aghtfghkofgh'))