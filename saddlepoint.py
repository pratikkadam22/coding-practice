def allSaddles(matrix):
    rowmins = []
    rowmaxs = []
    colmins = []
    colmaxs = []

    for i,row in enumerate(matrix):
        m = min(row)
        M = max(row)
        for j,x in enumerate(row):
            if x == m: rowmins.append((i,j))
            if x == M: rowmaxs.append((i,j))

    t = [list(column) for column in zip(*matrix)] #transpose of matrix

    for j,col in enumerate(t): 
        m = min(col)
        M = max(col)
        for i,x in enumerate(col):
            if x == m: colmins.append((i,j))
            if x == M: colmaxs.append((i,j))

    return (set(rowmins) & set(colmaxs)) | (set(rowmaxs) & set(colmins))

M = [[1,1,2,5,6,1],    
[5,6,8,5,6,7],
[10,12,10,12,11,11],
[8,10,5,6,8,9],
[6,5,10,12,15,19]]

print(allSaddles(M))