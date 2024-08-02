# 실행시간: 4684 ms
# 메모리: 34112 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/16234
# Reference: 

import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    que = deque()
    que.append((a, b))
    union = []
    union.append((a, b))
    
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    union.append((nx, ny))
    
    if len(union) <= 1:
        return 0
    
    population = sum(graph[x][y] for x, y in union) // len(union)
    for x, y in union:
        graph[x][y] = population
    
    return 1
    
            
day = 0
while True:
    stop = 0
    visited = [[False]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                stop += bfs(i, j)
    if stop == 0:
        break
    day += 1
print(day)