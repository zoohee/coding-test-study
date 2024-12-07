# 실행시간: 60 ms
# 메모리: 34176 KB
# 난이도: Gold 2
# Url: https://www.acmicpc.net/problem/17244
# Reference:
from itertools import permutations
from collections import deque 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y, idx):
    que = deque()
    que.append((x, y))
    visited = [[0] * n for _ in range(m)]
    visited[x][y] = 1
    
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == '#':
                    continue
                if graph[nx][ny] == 'X' or graph[nx][ny] == 'S' or graph[nx][ny] == 'E':
                    dist[idx][things.index((nx, ny))] = visited[x][y]
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
                
start = []
things = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'S':
            start.append((i, j))
        if graph[i][j] == 'E':
            end = (i, j)
        if graph[i][j] == 'X':
            things.append((i, j))
things.insert(0, start[0])
things.append(end)
dist = [[0] * len(things) for _ in range(len(things))]

for idx, data in enumerate(things):
    BFS(data[0], data[1], idx)
    
answer = 1e9
locations = [i + 1 for i in range(len(things) - 2)]
for p in list(permutations(locations)):
    nl = [0] + list(p) + [len(things) - 1]
    temp = 0
    for idx in range(1, len(nl)):
        temp += dist[nl[idx]][nl[idx - 1]]
    answer = min(answer, temp)

print(answer)