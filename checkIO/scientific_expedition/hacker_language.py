class HackerLanguage:
    def __init__(self):
        self.text = ''

    def delete(self, n):
        self.text = self.text[:-n]

    def write(self, msg):
        self.text += msg

    def send(self):

        def encrypt(to_encrypt):
            to_encrypt = bin(ord(to_encrypt))
            return to_encrypt[2:]

        special_signs = ['.', ':', '!', '?', '@', '$', '%']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        out = ''
        for letter in self.text:
            if letter not in digits and letter not in special_signs:
                if letter == ' ':
                    out += '1000000'
                else:
                    out += encrypt(letter)
            else:
                out += letter
        return out

    def read(self, msg):
        message = ""
        encrypted_message = msg
        while len(encrypted_message) > 0:
            decrypted_c = None
            binary = encrypted_message[:7]
            if binary.count("1") + binary.count("0") == 7:
                if binary == "1000000":
                    decrypted_c = " "
                else:
                    decrypted_c = chr(int(binary, 2))
                encrypted_message = encrypted_message[7:]
            else:
                decrypted_c = encrypted_message[0]
                encrypted_message = encrypted_message[1:]
            message += decrypted_c
        return message

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
