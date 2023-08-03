# 2718
# 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

def BFS(x, y):
    queue = deque() 
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i] # (1,0) (0,1) (-1,0) (0,-1)
            ny = y + dy[i] # 좌상우하 방문
            
            if 0 <= nx < n and 0 <= ny < m: # 그래프 크기 안이면    
                if graph[nx][ny] == 1: # 그래프 원소가 1이면
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    
    return graph[n-1][m-1]

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(BFS(0, 0))