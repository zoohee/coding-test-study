import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    que = deque([(x, y)])
    visited[x][y] = 1
    seaList = []
    
    while(que):
        x, y = que.popleft();
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 주변이 0이면 바다
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    que.append((nx, ny))  
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y , sea))
    for x, y, sea in seaList:
        # 마이너스면 0 저장
        graph[x][y] = max(0, graph[x][y] - sea)
    return 1
    
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            ice.append((i, j))
     
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
year = 0
       
# 빙산인 애들 bfs 시작
while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1
    
if group < 2:
    print(0)
    
    