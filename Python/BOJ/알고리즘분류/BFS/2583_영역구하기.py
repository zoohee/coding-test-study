from collections import deque
import sys
input = sys.stdin.readline

def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 1
    cnt = 1
    
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny]==0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
    result.append(cnt)
    
    
M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]

for i in range(K):
    startX, startY, endX, endY = map(int, input().split())
    for a in range(startX, endX):
        for b in range(M - startY - 1, M - endY - 1, -1):
            graph[b][a] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            BFS(i, j)

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')