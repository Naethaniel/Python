# You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:
#
# The initial and final markers are always different.
# If there is no initial marker then the beginning should be considered as the beginning of a string.
# If there is no final marker then the ending should be considered as the ending of a string.
# If the initial and final markers are missing then simply return the whole string.
# If the final marker is standing in front of the initial one then return an empty string.
# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
#
# Output: A string.
#
# Precondition: can't be more than one final marker and can't be more than one initial

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    try:
        beginIndex = text.index(begin)
    except ValueError:
        beginIndex = 0
        begin = ''
    try:
        endIndex = text.index(end)
    except ValueError:
        word = text[beginIndex + len(begin):]
        return word
    word = text[beginIndex+len(begin):endIndex]
    return word

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
