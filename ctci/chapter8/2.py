# 8.2: Robot in a Grid

def get_path(matrix):
    if not matrix:
        return 0
    visited = set()
    path = []
    if (get_path_helper(matrix, visited, len(matrix) - 1, len(matrix[0]) - 1, path)):
        return path
    return None

def get_path_helper(matrix, visited, row, col, path):
    if row < 0 or col < 0 or not matrix[row][col]:
        return False
    
    if (row, col) in visited:
        return False
    
    is_at_origin = (row == 0) and (col == 0)

    if (get_path_helper(matrix, visited, row - 1, col, path) or get_path_helper(matrix, visited, row, col - 1, path) or is_at_origin):
        path.append((row, col))
        return True
    
    return False

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,None,4],[5,6,7,None],[None,10,11,12]]
matrix = [[1,None,3,4],[5,6,7,None],[None,None,None,12]]

print(get_path(matrix))
    