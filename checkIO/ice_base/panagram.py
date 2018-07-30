import string
def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    text = text.lower()
    letters = list(string.ascii_lowercase)

    for letter in text:
        if letter in letters:
            letters.remove(letter)

    if len(letters) == 0:
        return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')
