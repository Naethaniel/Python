def popular_words(text: str, words: list) -> dict:
    # your code here
    text = text.lower()
    text = text.replace('\n', ' ')
    split = text.split(' ')
    myDict = {}
    for word in words:
        myDict[word] = 0
        for elem in split:
            if elem == word:
                myDict[word] += 1
    print(myDict)
    return myDict



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }

