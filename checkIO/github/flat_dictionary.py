def recurse_flatten(dictionary):
    output = {}

    for elem in dictionary:
        if type(dictionary[elem]) is not dict:
            output[elem] = dictionary[elem]
        else:
            if dictionary[elem] == {}:
                output[elem] = ''
            else:
                after = recurse_flatten(dictionary[elem])
                for a in after:
                    output[elem + '/' + a] = after[a]
    return output


def flatten(dictionary):
    resp = recurse_flatten(dictionary)
    return resp


if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')

print(flatten(
    {"key": {"deeper": {"more": {"enough": "value"}}}}))