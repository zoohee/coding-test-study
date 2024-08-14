# 실행시간: 40 ms
# 메모리: 31120 KB
# 난이도: Gold 3
# Url: https://www.acmicpc.net/problem/15685
# Reference: https://tmdrl5779.tistory.com/146

import sys
input = sys.stdin.readline
n = int(input())

graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):

    y, x, d, g = map(int, input().split(' '))
    graph[x][y] = 1

    curve = [d]
    for j in range(g):
        for k in range(len(curve) - 1, -1, -1):
            curve.append((curve[k] + 1) % 4)

    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        if 0 <= x < 101 and 0 <= y < 101:
            graph[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)