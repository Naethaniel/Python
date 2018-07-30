def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here

    ret = 0
    for elems in t:
        if type(elems) == int:
            if elems >= ret:
                ret = elems
        if type(elems) == tuple:
            m = max_val(elems)
            if m >= ret:
                ret = m
        if type(elems) == list:
            m = max_val(elems)
            if m >= ret:
                ret = m
    return ret



# max_val((5, (1,2), [[1],[2]])) returns 5.
# max_val((5, (1,2), [[1],[9]])) returns 9.

max_val((5, (1,2), [[1],[2]]))
max_val((5, (1,2), [[1],[9]]))