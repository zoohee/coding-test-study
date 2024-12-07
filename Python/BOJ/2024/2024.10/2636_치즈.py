# 실행시간: 72 ms
# 메모리: K34096 B
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/2636
# Reference: 
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = []
cheeze = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    cheeze += sum(graph[i])
    
def bfs():
    que = deque()
    que.append((0, 0))
    melt = deque()
    
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0: 
                    que.append((nx, ny))
                elif graph[nx][ny] == 1:
                    melt.append((nx, ny))
    
    for x, y in melt:
        graph[x][y] = 0
        
    return len(melt)
    
    
time = 1
while True:
    visited = [[0]*m for _ in range(n)]
    cnt = bfs()
    cheeze -= cnt
    
    if cheeze == 0:
        print(time)
        print(cnt)
        break
    time += 1
    

