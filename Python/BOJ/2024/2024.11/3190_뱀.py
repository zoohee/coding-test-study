# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
    
def dummy():
    sec = 1
    nx, ny = 0, 0
    graph[0][0] = 2
    d = 0
    
    snake = deque()
    snake.append((0, 0))
    while True:
        nx = nx + dx[d]
        ny = ny + dy[d]
        snake.append((nx, ny))
        
        # 벽과 부딪히면 끝
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            return sec
        
        # 자기 자신과 부딪히면 끝
        if graph[nx][ny] == 2:
            return sec
        
        if graph[nx][ny] == 1:
            graph[nx][ny] = 2
            
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            a, b = snake.popleft()
            graph[a][b] = 0
        
        if sec in info.keys():
            if info[sec] == 'L':
                d = (d - 1 + 4) % 4
            else:
                d = (d + 1) % 4
        
        sec += 1

n = int(input())
graph = [[0] * n for _ in range(n)] # 0: 빈칸 1: 사과칸 2: 뱀칸

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

l = int(input())
info = {}
for _ in range(l):
    t, c = input().split()
    info[int(t)] = c
    
print(dummy())