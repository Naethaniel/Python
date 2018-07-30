import string
def checkio(text: str) -> str:

    #replace this for solution
    data = text.lower()
    dict = {}
    if len(data) == 1:
        return data[0]
    for elem in data:
        if elem in dict.keys():
            dict[elem] += 1
        else:
            dict[elem] = 1
    best = 0
    res = ''
    for elem in dict:
        if elem in string.ascii_lowercase:
            if dict[elem] > best:
                res = elem
                best = dict[elem]
            elif dict[elem] == best:
                if str(elem) < str(res):
                    res = elem
                    best = dict[elem]
    return res

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
