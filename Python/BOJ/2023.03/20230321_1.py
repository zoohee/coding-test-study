#7576
#토마토
from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
queue = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1
            
BFS()

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]!= -1 and visited[i][j] == 0:
            print(-1)
            exit(0)
        answer = max(answer, visited[i][j])

print(answer-1)

            
        