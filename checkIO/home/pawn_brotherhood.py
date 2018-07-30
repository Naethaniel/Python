def safe_pawns(pawns: set) -> int:
    pawns_indexes = set()
    safe = 0
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
    for pair in pawns_indexes:
        first = (pair[0]-1, pair[1]+1)
        second = (pair[0]-1, pair[1]-1)
        if first in pawns_indexes or second in pawns_indexes:
            safe += 1
    return safe


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
