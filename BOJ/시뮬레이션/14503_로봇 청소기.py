# 시간복잡도: 
# 최악시간: 
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/14503
# Reference: 
import sys
input = sys.stdin.readline
from collections import deque

def BFS(r, c, d):
    visited[r][c] = 1
    cnt = 1
    
    while True:
        check = 0
        
        for _ in range(4):
            d = (d+3) % 4
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    r ,c = nr, nc
                    cnt += 1
                    check = 1
                    break
        
        if check == 0:
            if room[r-dr[d]][c-dc[d]] == 1:
                print(cnt)
                break
            else:
                r, c = r-dr[d], c-dc[d]     
            
    
# 로봇이 반시계로 돌려면 방이 시계방향
# 회전할 때 마다 가로 세로가 달라짐
def rotate(a, b):
    global robot
    tmp = [[0] * b for _ in range(a)]
    tmp_v = [[0] * b for _ in range(a)]
    for i in range(b):
        for j in range(a):
            if robot == (b-j, i):
                robot = (i, j)
            tmp[i][j] = room[b-j][i]
            tmp_v[i][j] = visited[b-j][i]
    return tmp, tmp_v
    
    
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# dr = (0, 1, 0, -1)
# dc = (-1, 0, 1, 0)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

BFS(r, c, d)
# d가 0인 경우 북쪽, 1인 경우 동쪽, 
# 2인 경우 남쪽, 3인 경우 서쪽
# 0: 청소되지 않은 빈 칸, 1: 벽이 있는 칸
# 로봇 청소기가 있는 칸은 항상 빈 칸
