# 실행시간: 40ms
# 메모리: 31120KB
# 난이도: Silver 4
# Url: https://www.acmicpc.net/problem/1205
# Reference: me
import sys
input = sys.stdin.readline

n, new, p = map(int, input().split())
if n==0:
    print(1)
    exit(0)
else:
    score = list(map(int, input().split()))
    if n == p and score[-1] >= new:
        print(-1)
    else:
        ans = n + 1
        for i in range(n):
            if score[i] <= new:
                ans = i + 1
                break
        print(ans)