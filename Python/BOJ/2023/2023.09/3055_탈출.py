import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = []
que = deque()

for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'D':
            end = (i, j)
        elif graph[i][j] == '*':
            que.append((i, j, '*'))
        elif graph[i][j] == 'S':
            start = (i, j, 0)
que.append(start)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while(que):
    x, y, z = que.popleft()
    if x == end[0] and y==end[1]: # D에 도착
        print(z)
        break
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx <n and 0 <= ny < m:
            # 물을 먼저 채우고
            if z == '*' and (graph[nx][ny] == '.' or graph[nx][ny] == 'S'):
                graph[nx][ny] = '*'
                que.append((nx, ny, '*'))
            # 고슴도치 이동
            elif z != '*' and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
                graph[nx][ny] = 'S'
                que.append((nx, ny, z+1))
                
    if len(que)==0:
        print('KAKTUS')
        break  
            