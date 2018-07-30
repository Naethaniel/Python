DIGITS = {
    "0": ['a', 'b', 'c', 'd', 'e', 'f'],
    "1": ['b', 'c'],
    "2": ['a', 'b', 'd', 'e', 'g'],
    "3": ['a', 'b', 'c', 'd', 'g'],
    "4": ['b', 'c', 'f', 'g'],
    "5": ['a', 'c', 'd', 'f', 'g'],
    "6": ['a', 'c', 'd', 'e', 'f', 'g'],
    "7": ['a', 'b', 'c'],
    "8": ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    "9": ['a', 'b', 'c', 'd', 'f', 'g']
}


def seven_segment(lit_seg, broken_seg):
    def is_slice_in_list(s, l):
        len_s = len(s)  # so we don't recompute length of s on every iteration
        return any(s == l[i:len_s+i] for i in range(len(l) - len_s+1))

    first_display = {
        "working": [],
        "broken": []
    }
    second_display = {
        "working": [],
        "broken": []
    }
    possibilities_first = []
    digits_first = []
    possibilities_second = []
    digits_second = []

    for letter in lit_seg:
        if letter.isupper():
            first_display['working'] += [letter.lower()]
        else:
            second_display['working'] += [letter]

    for letter in broken_seg:
        if letter.isupper():
            first_display['broken'] += [letter.lower()]
        else:
            second_display['broken'] += [letter]

    for key, digits in DIGITS.items():
        if len(first_display['broken']) > 0:
            if is_slice_in_list(first_display['working'], digits):
                possibilities_first.append(key)
        else:
            if all(elem in first_display['working'] for elem in digits):
                digits_first.append(key)
        if len(second_display['broken']) > 0:
            if is_slice_in_list(second_display['working'], digits):
                possibilities_second.append(key)
        else:
            if all(elem in second_display['working'] for elem in digits):
                digits_second.append(key)

    if len(digits_first) == 0:
        first_display['working'] += first_display['broken']
        for key, digits in DIGITS.items():
            if all(elem in first_display['working'] for elem in digits):
                digits_first.append(key)
    if len(digits_second) == 0:
        second_display['working'] += second_display['broken']
        for key, digits in DIGITS.items():
            if all(elem in second_display['working'] for elem in digits):
                digits_second.append(key)

    print(list(set(possibilities_first) & set(digits_first)), list(set(possibilities_second) & set(digits_second)))
    print(digits_first, digits_second)
    print(len(digits_first)*len(digits_second))
    return len(list(set(possibilities_first) & set(digits_first)))*len(list(set(possibilities_second) & set(digits_second)))


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')