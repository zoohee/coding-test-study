# 실행시간: 2844 ms
# 메모리: 31120 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/17144
# Reference: 
import sys
from collections import deque
input = sys.stdin.readline
r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1
for i in range(r):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

que = []
cleaner = []
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        tmp_arr[nx][ny] += graph[i][j] // 5
                        tmp += graph[i][j] // 5
                graph[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            graph[i][j] += tmp_arr[i][j]

def clean_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny


def clean_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

for _ in range(t):
    spread()
    clean_up()
    clean_down()

answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)