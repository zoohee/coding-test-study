# 실행시간: 160 ms
# 메모리: 37996 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/14500
# Reference: 
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tetromino = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1]
visited = [([0] * m) for _ in range(n)]
maximum = max(map(max, tetromino))

def DFS(x, y, idx, total):
    global a
    if a >= total + maximum * (3 - idx):
        return
    if idx == 3:
        a = max(a, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if idx == 1:  # ㅗ 모양
                    visited[nx][ny] = 1
                    DFS(x, y, idx + 1, total + tetromino[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                DFS(nx, ny, idx+1, total + tetromino[nx][ny])
                visited[nx][ny] = 0

a = 0    
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        DFS(i, j, 0, tetromino[i][j])
        visited[i][j] = 0

print(a)