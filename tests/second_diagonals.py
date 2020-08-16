# CodeSignal Question
# Given a square matrix, return a list of all the diagonals parallel to the secondary diagonal(matrix[i][n-i-1])
# in a sorted order (including the secondary diagonal itself).
# For example: the result for the input matrix should be:
# [[8],
#  [3,9],
#  [2,3,5],
#  [1,3,4,6],
#  [1,4,6],
#  [2,9],
#  [0]]

def second_diagonals(matrix):
    res, n = [], len(matrix)
    while n != 0:
        curr = []
        for i in range(0, n):
            curr.append(matrix[i][n - 1 - i])
        res.append(sorted(curr))
        n -= 1
    start, n = 1, len(matrix)
    while n != start:
        curr = []
        for i in range(start, n):
            curr.append(matrix[i][n - i + start - 1])
        res.append(sorted(curr))
        start = start + 1
    return res

matrix=[[8,3,2,1],
        [9,3,6,4],
        [5,3,6,9],
        [4,1,2,0]]
res = second_diagonals(matrix)
print(res)