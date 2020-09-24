# 8.10: Paint Fill

def paint_fill_util(M, N, screen, x, y, prevC, newC):
    if(x < 0 or x >= M or y < 0 or y >= N or screen[x][y] != prevC or screen[x][y] == newC):
        return
        
    screen[x][y] = newC
        
    paint_fill_util(M, N, screen, x+1, y, prevC, newC)
    paint_fill_util(M, N, screen, x-1, y, prevC, newC)
    paint_fill_util(M, N, screen, x, y+1, prevC, newC)
    paint_fill_util(M, N, screen, x, y-1, prevC, newC)
        
def paint_fill(image, sr, sc, newColor):
    M = len(image)
    N = len(image[0])
    prevColor = image[sr][sc]
    paint_fill_util(M, N, image, sr, sc, prevColor, newColor)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
res = paint_fill(image, sr, sc, newColor)
print(res)
        