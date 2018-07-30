def to_encrypt(text, delta):
    output = ''
    if delta > 0:
        for letter in text:
            if letter == ' ':
                output += letter
            else:
                i = ord(letter)
                i += delta
                while not 97 <= i <= 122:
                    i -= 26
                output += chr(i)
    else:
        for letter in text:
            if letter == ' ':
                output += letter
            else:
                i = ord(letter)
                i += delta
                while not 97 <= i <= 122:
                    i += 26
                output += chr(i)
    return output


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
