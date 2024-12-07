# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    que = deque()
    que.append((0, 0))
    visited[0][0] = 0
    
    while que:
        x, y = que.popleft()
        if x == n-1 and y == n-1:
            return visited[x][y]
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] == '1':
                    que.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    que.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    
    
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]

print(bfs())