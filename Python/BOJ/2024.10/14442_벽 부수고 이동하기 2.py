# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference:
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    global k
    que = deque()
    que.append((0, 0, k))
    visited[0][0][k] = 1

    while que:
        x, y, c = que.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][c]
            
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    que.append((nx, ny, c))
                    visited[nx][ny][c] = visited[x][y][c] + 1
                elif graph[nx][ny] == 1 and c > 0 and visited[nx][ny][c-1] == 0:
                    que.append((nx, ny, c-1))
                    visited[nx][ny][c-1] = visited[x][y][c] + 1

    return -1
            
            

n, m, k = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

print(bfs())

# 5 5 3
# 01011
# 00111
# 11100
# 11101
# 11110
