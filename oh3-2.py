#3-2

VOID, WALL, VISITED = 0, 1, 2
def rec(x,y):
    global grid
    if grid[x][y] == VISITED:
        return False
    
    grid[x][y] = VISITED
    if x == y == n:
        return True
    
    for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
        nx, ny = x, y
        while grid[nx][ny] != WALL:
            nx, ny = nx+dx, ny+dy
        if rec(nx-dx, ny-dy):
            return True
    return False
        
    
for i in range(int(input())):
    n = int(input())
    grid = [list(map(int,input().split())) for j in range(n)]
    for g in grid:
        g.insert(n, WALL)
        g.insert(0, WALL)
    grid.insert(n, [1]*(n+2))
    grid.insert(0, [1]*(n+2))
    print('YES' if rec(1, 1) else 'NO')
    #break
    
