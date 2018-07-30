VOWELS = "aeiouy"

def translate(phrase):
    phrase = phrase.split(' ')
    output = []
    for word in phrase:
        pos = 0
        curr_word = ''
        while True:
            try:
                if word[pos] not in VOWELS:
                    curr_word += word[pos]
                    pos += 2
                else:
                    curr_word += word[pos]
                    pos += 3
            except IndexError:
                break
        output.append(curr_word)
    return ' '.join(output)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

print(translate("hieeelalaooo"))
print(translate("hoooowe yyyooouuu duoooiiine"))