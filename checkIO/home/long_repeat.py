def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    if len(line) == 0:
        return 0
    li = ''
    repeats = []
    for i in range(len(line)):
        li += line[i]
        if len(li) != 1:
            if li[-1] != li[-2]:
                li = li[:-1]
                repeats.append(li)
                li = line[i]
    if len(repeats) == 0:
        repeats.append(li)
    return len(max(repeats, key=len))




# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert long_repeat('sdsffffse') == 4, "First"
#     assert long_repeat('ddvvrwwwrggg') == 3, "Second"
#     assert long_repeat('abababaab') == 2, "Third"
#     assert long_repeat('') == 0, "Empty"
print(long_repeat('sdsffffse'))
print(long_repeat("aa"))


