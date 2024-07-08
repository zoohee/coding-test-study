# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [[False]*m for _ in range(n)]

k_que = deque()
q_que = deque()
for name in range(3):
    arr = list(map(int, input().split()))
    N = arr[0]
    if name==0: #queen
        for i in range(N):
            q_que.append((arr[2*i+1]-1, arr[2*i+2]-1))
            board[arr[2*i+1]-1][arr[2*i+2]-1] = True
    elif name==1: #knight
        for i in range(N):
            k_que.append((arr[2*i+1]-1, arr[2*i+2]-1))
            board[arr[2*i+1]-1][arr[2*i+2]-1] = True
    else: #pawn
        for i in range(N):
            board[arr[2*i+1]-1][arr[2*i+2]-1] = True


kx = [1,2,2,1,-1,-2,-2,-1]
ky = [-2,-1,1,2,2,1,-1,-2]
while(k_que):
    x, y = k_que.popleft()
    for i in range(8):
        nx = x + kx[i]
        ny = y + ky[i]
        if(nx >= n or nx < 0  or ny >= m or ny < 0 or board[nx][ny]==True):
            continue
        board[nx][ny]=True
    

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]
while(q_que):
    x, y = q_que.popleft()
    board[x][y] = True
    
    for d in range(8):
        # 같은 방향으로만 들어가야 됨
        nx = x + dx[d]
        ny = y + dy[d]
        if(nx >= n or nx < 0  or ny >= m or ny < 0 or board[nx][ny]==True):
            continue
        
        board[nx][ny] = True
        q_que.append((nx, ny))
        print((nx,ny))

for i in range(n):
    print(board[i])
            
    
    
    
# arr = list(map(int, input().split()))
# q = arr[0]
# queens = [(0,0) for _ in range(q)]
# for i in range(q):
#     queens[i] = (arr[2*i+1], arr[2*i+2])
    

# arr = list(map(int, input().split()))
# k = arr[0]
# knights = [(0,0) for _ in range(k)]
# for i in range(k):
#     knights[i] = (arr[2*i+1], arr[2*i+2])
    
# arr = list(map(int, input().split()))
# p = arr[0]
# pawns = [(0,0) for _ in range(p)]
# for i in range(p):
#     pawns[i] = (arr[2*i+1], arr[2*i+2])
    
# print(queens)
# print(knights)
# print(pawns)