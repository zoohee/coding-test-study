# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((b, a))
arr.sort(key = lambda x: (x[0], -x[1]))

answer = sys.maxsize
w, s = 0, 0
flag = False

for i in range(n):
    w += arr[i][1]
    if i >= 1 and arr[i][0] == arr[i-1][0]:
        s += arr[i][0]
    else:
        s = 0
    if w >= m:
        answer = min(answer, arr[i][0] + s)
        flag = True

print(answer if flag else -1)