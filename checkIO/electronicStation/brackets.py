def checkio(expression):
    dict = []
    opBrackets = ['{', '(', '[']
    closBrackets = ['}', ')', ']']
    for letter in expression:
        if letter in opBrackets:
            dict.append(letter)
        if letter in closBrackets:
            try:
                pos = opBrackets.index(dict[-1])
            except IndexError:
                return False
            if closBrackets[pos] != letter:
                return False
            else:
                dict.pop()
    if len(dict) > 0:
        return False
    return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

print(checkio("(((1+(1+1))))]"))