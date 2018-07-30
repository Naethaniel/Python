# Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list [[10, 4, 6, 8],
# [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]
# #
# # Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list [[1, 1], [1, 1], [1, 1], [1, 4]]

def getSublists(L, n):
    index = 0
    result = []
    current = []

    outputs = len(L) - n + 1

    for i in range(0,outputs):
        for j in range(0, n):
            current.append(L[index + j])
        result.append(current)
        current = []
        index += 1
    return result


L = [1, 1, 1, 1, 4]
print(getSublists(L, 2))
# [[1, 1], [1, 1], [1, 1], [1, 4]
