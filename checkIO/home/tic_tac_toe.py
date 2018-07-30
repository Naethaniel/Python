from typing import List

def checkio(game_result: List[str]) -> str:
    # vertical
    for i in range(3):
        pivot = game_result[0][i]
        if pivot != '.':
            if pivot == game_result[1][i] and pivot == game_result[2][i]:
                return pivot
    # horizontal
    for i in range(3):
        pivot = game_result[i][0]
        if pivot != '.':
            if pivot == game_result[i][1] and pivot == game_result[i][2]:
                return pivot
    # diagonal
    middle = game_result[1][1]
    if middle != '.':
        if middle == game_result[0][0] and middle == game_result[2][2]:
            return middle
        if middle == game_result[0][2] and middle == game_result[2][0]:
            return middle
    return 'D'

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
