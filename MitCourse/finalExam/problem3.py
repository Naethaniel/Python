def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    sum = 1
    counter = 2
    if sum == k:
        return True

    while sum <= k:
        if sum == k:
            return True
        else:
            sum += counter
            counter += 1
    return False


def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here
    largest = 0
    times = 0

    while True:
        if len(L) == 0 and largest == 0:
            return None
        for elem in L:
            if elem == largest:
                times += 1
            if elem > largest:
                largest = elem
                times = 1
        if times % 2 != 0:
            return largest
        elif len(L) > 0:
            L = list(filter(lambda a: a != largest, L))
            largest = 0
            times = 0
        else:
            return None
# largest_odd_times([2,2,4,4]) returns None
# largest_odd_times([3,9,5,3,5,3]) returns 9

# print(largest_odd_times([2, 2, 4, 4]))
# print(largest_odd_times([3, 9, 5, 3, 5, 3]))

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    myDict = {}
    word = ''
    for i in range(len(map_from)):
        myDict[map_from[i]] = map_to[i]
    for letter in code:
        word += myDict[letter]
    return myDict, word



# cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same)
#  ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
print(cipher("abcd", "dcba", "dab"))