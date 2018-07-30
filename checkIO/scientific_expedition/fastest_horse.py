def fastest_horse(horses: list) -> int:
    di = {}

    for elems in horses:
        fastest = elems.index(min(elems))
        try:
            di[fastest + 1] += 1
        except KeyError:
            di[fastest + 1] = 1
    return max(di, key=di.get)



if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))
    print(fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]))
    print(fastest_horse([["4:44", "4:11", "4:18"], ["3:10", "3:01", "3:14"], ["2:20", "2:23", "2:15"]]))

    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    # print("Coding complete? Click 'Check' to earn cool rewards!")