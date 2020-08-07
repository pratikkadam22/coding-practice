map_ = {
1 : [2, 3, 4, 7],
2 : [1, 3, 5, 8],
3 : [1, 2, 6, 9],
4 : [1, 7, 5, 6],
5 : [2, 8, 4, 6],
6 : [3, 9, 4, 5],
7 : [1, 4, 8, 9],
8 : [2, 5, 7, 9],
9 : [3, 6, 7, 8]
}
    
def backtrack(res, curr):
    if len(curr) == 3:
        res.append(curr[:])
        return
        
    for ele in map_[curr[-1]]:
        curr.append(ele)
        backtrack(res, curr)
        curr.pop()
    
res, curr = [], [4]
backtrack(res, curr)
print(res)