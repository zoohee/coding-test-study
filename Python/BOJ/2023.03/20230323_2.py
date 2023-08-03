#10026
#적록색약
from collections import deque
import sys
input = sys.stdin.readline

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    
    while(queue):
        x, y = queue.popleft()
        color = graph[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if color == graph[nx][ny] and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
  
answer = 0      
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            BFS(i, j)
            answer += 1
print(answer, end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]
answer = 0      
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            BFS(i, j)
            answer += 1
print(answer)