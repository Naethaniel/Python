def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    myDict = {}
    result = []

    # count appearance
    # return only 1's


    for val in aDict:
        if val not in myDict:
            myDict[val] = 0
        else:
            myDict[val] += 1

    for val in myDict:
        if myDict[val] == 0:
            result.append(val)
    result.sort()
    return result

print(uniqueValues({2: 0, 3: 3, 6: 1}))
print(uniqueValues({1: 1, 2: 2, 3: 3}))
print(uniqueValues({1: 1, 2: 1, 3: 1}))

