def rec(x, y, k):
    global n, grid

    if x < 0 or y < 0 or n <= x or n <= y or grid[x][y]: # 칸을 넘겼거나 빈 칸이 아닐 때
        return 0
    
    if x == n-1 and y == n-1: # 도착하면
        return 1

    if not k: # 남은 발걸음이 0일 때
        return 0

    grid[x][y] = 2 # 방문한 곳은 2로
    count = sum(rec(x+dx, y+dy, k-1) for dx,dy in (1,0), (0,1), (-1,0), (0,-1))
    grid[x][y] = 0
    return count
        
for i in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split())) for i in range(n)]
    k = int(input())
    print(rec(0, 0, k))
