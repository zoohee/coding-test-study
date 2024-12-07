# 실행시간: 44 ms
# 메모리: 31120 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/2011
# Reference: https://jyeonnyang2.tistory.com/55
import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
if n[0] == 0:
    print(0)
    exit(0)

l = len(n)
n = [0] + n
dp = [0 for _ in range(l+1)]
dp[0], dp[1] = 1, 1

for i in range(2, l+1):
    if n[i] > 0:
        dp[i] += dp[i-1]
    tmp = n[i-1] * 10 + n[i]
    if 10 <= tmp <= 26:
        dp[i] += dp[i-2]

print(dp[l] % 1000000)