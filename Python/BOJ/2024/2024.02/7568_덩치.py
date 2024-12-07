# 실행시간: 40ms
# 메모리: 31120KB
# 난이도: Silver 5
# Url: https://www.acmicpc.net/problem/7568
# Reference: me
import sys
input = sys.stdin.readline
n = int(input())

size = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            cnt += 1
    ans.append(cnt+1)

for i in range(n):
    print(ans[i], end=" ")