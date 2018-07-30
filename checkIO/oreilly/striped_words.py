import string
VOWELS = "AEIOUYaeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"


def checkio(text):

    count = 0
    stripes = 0
    pos = 0

    text = text.replace(',', ' ').replace('.', ' ').replace('?', ' ').split()

    for word in text:
        while pos != len(word):
            try:
                letter = word[pos]
                next_letter = word[pos + 1]
            except IndexError:
                break
            if letter in VOWELS and next_letter not in CONSONANTS:
                break
            elif letter in CONSONANTS and next_letter not in VOWELS:
                break
            if letter.isdigit() or next_letter.isdigit():
                pos += 1
                break
            stripes += 1
            pos += 1
        if stripes == len(word)-1 and len(word) != 1:
            count += 1
        stripes = 0
        pos = 0
    return count

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio("My name is ...") == 3, "All words are striped"
#     assert checkio("Hello world") == 0, "No one"
#     assert checkio("A quantity of striped words.") == 1, "Only of"
#     assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

print(checkio("1st 2a ab3er root rate"))
