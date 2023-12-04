# 실행시간: 72ms
# 메모리: 34096KB
# 난이도: Silver 1
# Url: https://www.acmicpc.net/problem/1303
# Reference: me
import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True
    s = graph[i][j]
    cnt = 1
    
    while(que):
        x, y = que.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny]==s and visited[nx][ny]==False:
                    cnt += 1
                    visited[nx][ny]=True
                    que.append((nx, ny))
    
    return cnt

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
W = 0
B = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            if graph[i][j] == 'W':
                w = bfs(i, j)
                W += w*w
            else:
                b = bfs(i, j)
                B += b*b

print(W,B)
# 81+49
# 64+1