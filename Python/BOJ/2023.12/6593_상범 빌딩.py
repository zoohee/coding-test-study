# 실행시간: 140ms
# 메모리: 34116KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/6593
# Reference: Me + gpt

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, z):
    que = deque()
    que.append((x, y, z))
    time[x][y][z] = 1
    while que:
        x, y, z = que.popleft()
        
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if building[nx][ny][nz] == 'E':
                    print("Escaped in", time[x][y][z], "minute(s).")
                    return
                
                if building[nx][ny][nz] == '.' and time[nx][ny][nz] == 0:
                    time[nx][ny][nz] = time[x][y][z] + 1
                    que.append((nx, ny, nz))
                            
    print("Trapped!")   

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while(True):
    l, r, c = map(int, input().split())
    
    if l == 0 and r == 0 and c == 0:
        break
    
    building = []
    time = [[[0]*c for _ in range(r)] for _ in range(l)]
    for _ in range(l):
        floor = [list(input().rstrip()) for _ in range(r)]
        building.append(floor)
        input().rstrip()
        
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    bfs(i, j, k)
    
    