class Capital(object):
    __instance = None

    def __new__(cls, val):
        if Capital.__instance is None:
            Capital.__instance = object.__new__(cls)
            Capital.__instance.val = val
        return Capital.__instance

    def name(self):
        return self.val



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    print(ukraine_capital_2.name())

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")