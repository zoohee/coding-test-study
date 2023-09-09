import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    que = deque()
    que.append((0, 0, 0))
    
    while(que):
        x, y, z = que.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]+1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 1 and z == 0 :
                visited[nx][ny][1] = visited[x][y][0] + 1 # 뿌신다
                que.append((nx, ny, 1))
            
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                que.append((nx, ny, z))
                
    return -1
        
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

print(bfs())