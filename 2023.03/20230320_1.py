#4179
#불
from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    while(f_queue):
        x, y = f_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != '#' and not f_visited[nx][ny]:
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append((nx, ny)) 
    
    while(j_queue):
        x, y = j_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '.' and j_visited[nx][ny] == 0:
                    if f_visited[nx][ny] == 0 or f_visited[nx][ny] > j_visited[x][y] + 1:
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_queue.append((nx, ny))
            else: #상하좌우 중 한 곳이 graph 밖일 때
                return j_visited[x][y]
    
    return "IMPOSSIBLE"


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
f_visited = [[0] * c for _ in range(r)]
j_visited = [[0] * c for _ in range(r)]
f_queue = deque()
j_queue = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            f_queue.append((i, j))
            f_visited[i][j] = 1
        if graph[i][j] == 'J':
            j_queue.append((i, j))
            j_visited[i][j] = 1
            
print(BFS())