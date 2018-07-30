class Friends:

    def __init__(self, connections):
        self.connections = set()
        for elem in connections:
            if elem not in self.connections:
                self.connections.add(frozenset(elem))

    def add(self, connection):
        if connection not in self.connections:
            self.connections.add(frozenset(connection))
            return True
        else:
            return False

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(frozenset(connection))
            return True
        else:
            return False

    def names(self):
        output = set()
        for key, value in self.connections:
            if key not in output:
                output.add(key)
            if value not in output:
                output.add(value)
        return output

    def connected(self, name):
        output = set()
        for key, value in self.connections:
            if key == name:
                if value not in output:
                    output.add(value)
            if value == name:
                if key not in output:
                    output.add(key)
        return output



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
