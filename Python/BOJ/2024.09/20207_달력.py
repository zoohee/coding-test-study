# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
calendar = [0] * 366

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        calendar[i] += 1

row, col = 0, 0
answer = 0
for i in range(366):
    if calendar[i] != 0:
        row = max(row, calendar[i])
        col += 1
    else:
        answer += row * col
        row = 0
        col = 0

answer += row * col
print(answer)