animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    counter = 0
    for i in aDict:
        for e in aDict[i]:
            counter += 1
    return counter

print(how_many(animals))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    val = 0
    key = ''
    for i in aDict:
        curr = 0
        for elem in aDict[i]:
            curr += 1
        if curr > val:
            key = i
            val = curr
    return key

print(biggest(animals))
