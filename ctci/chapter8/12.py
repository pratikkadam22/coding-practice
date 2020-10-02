# 8.12: Eight Queens (LC 51. N-Queens)
# Complexity: O(n!)
# For complexity analysis: https://www.codesdope.com/course/algorithms-backtracking/

def place_queens(row, cols, res, grid_size):
    if row == grid_size:
        res.append(cols[:])
    else:
        for c in range(grid_size):
            if check_valid(row, c, cols):
                cols[row] = c
                place_queens(row + 1, cols, res, grid_size)

def check_valid(row1, col1, cols):
    for row2 in range(row1):
        col2 = cols[row2]
        if col1 == col2:
            return False
        col_dist = abs(col2 - col1)
        row_dist = row1 - row2
        if col_dist == row_dist:
            return False
    return True

def solveNQueens(n):
    grid_size = n
    cols = [0] * n
    res = []
    place_queens(0, cols, res, grid_size)
    grid = [["".join(["." for k in range(n)]) for j in range(n) ] for i in range(len(res))]
    for i in range(len(res)):
        for j in range(n):
            c = res[i][j]
            curr_row = grid[i][j]
            curr_row = curr_row[:c] + 'Q' + curr_row[c + 1:]
            grid[i][j] = curr_row
    return grid

ans = solveNQueens(8)
for i in range(len(ans)):
    print("Solution:", i + 1)
    for j in ans[i]:
        print(j)
    print('-------------------------')