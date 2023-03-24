from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    while(f_queue):
        x, y = f_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < c and 0 <= ny < r:
                if graph[nx][ny] != '#' and not f_visited[nx][ny]:
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append((nx, ny)) 
    
    while(j_queue):
        x, y = j_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < c and 0 <= ny < r:
                if graph[nx][ny] == '.' and j_visited[nx][ny] == 0:
                    if f_visited[nx][ny] == 0 or f_visited[nx][ny] > j_visited[x][y] + 1:
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_queue.append((nx, ny))
            else: 
                return j_visited[x][y]
    
    return "IMPOSSIBLE"

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
for i in range(n):
    r, c = map(int, input().split())
    graph = [list(input()) for _ in range(c)]
    f_visited = [[0] * r for _ in range(c)]
    j_visited = [[0] * r for _ in range(c)]
    f_queue = deque()
    j_queue = deque()
    
    for j in range(c):
        for k in range(r):
            if graph[j][k] == '*':
                f_queue.append((j, k))
                f_visited[j][k] = 1
            if graph[j][k] == '@':
                j_queue.append((j, k))
                j_visited[j][k] = 1
                
    print(BFS())