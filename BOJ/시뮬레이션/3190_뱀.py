# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/3190
# Reference: 
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
d = {}
for i in range(L):
    sec, direct = input().split()
    d[int(sec)] = direct
board = [[0] * N for _ in range(N)]
for i in range(len(apples)):
    board[apples[i][0]-1][apples[i][1]-1] = 1

snake = deque()
snake.append((0, 0))
r, c, time = 0, 0, 0
direction = 0 # 0, 1, 2, 3 동남서북
dr = [0,1,0,-1]
dc = [1,0,-1,0]
    
while(True):
    nr, nc = r+dr[direction], c+dc[direction]
    if nr<0 or nc<0 or nr>=N or nc>=N or (nr,nc) in snake:
        time += 1
        break
    if board[nr][nc] == 1:
        board[nr][nc] = 0
    else:
        snake.popleft()
    r, c = nr, nc
    snake.append((r, c))
    time += 1

    if time in d.keys():
        if d[time] == "D":
            direction = (direction+1)%4
        else:
            if direction == 0:
                direction = 3
            else:
                direction = direction - 1
    
print(time)