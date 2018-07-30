VOWELS = "aeiou"


class Chat:
    human_chat = ''
    robot_chat = ''

    def __init__(self):
        self.human = None
        self.robot = None

    def connect_human(self, human):
        self.human = human

    def connect_robot(self, robot):
        self.robot = robot

    def show_human_dialogue(self):
        return '{}'.format(self.human_chat[:-1])

    def show_robot_dialogue(self):
        return '{}'.format(self.robot_chat[:-1])



class Human:
    def __init__(self, name):
        self.name = name

    def send(self, msg):
        Chat.human_chat += '{} said: {}\n'.format(self.name, msg)
        out = ''
        for letter in msg:
            if letter in VOWELS:
                out += '0'
            else:
                out += '1'
        Chat.robot_chat += '{} said: {}\n'.format(self.name, out)

class Robot:
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def send(self, msg):
        Chat.human_chat += '{} said: {}\n'.format(self.serial_number, msg)
        out = ''
        for letter in msg:
            if letter in VOWELS:
                out += '0'
            else:
                out += '1'
        Chat.robot_chat += '{} said: {}\n'.format(self.serial_number, out)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    print(chat.show_human_dialogue())
    print(chat.show_robot_dialogue())
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new? 
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")