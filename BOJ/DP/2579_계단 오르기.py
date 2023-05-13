# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]
if len(s) == 1:
    print(s[0])
    exit(0)
elif len(s) == 2:
    print(s[0]+s[1])
    exit(0)
    
dp = [0] * (n+1)
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1]+s[2], s[0]+s[2])

for i in range(3, n):
    # 전계단과 현재계단 연속으로 밟기 vs 전전계단과 현재계단 밟기
    dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])

print(dp[n-1])    