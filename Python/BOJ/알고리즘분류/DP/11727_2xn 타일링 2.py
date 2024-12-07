# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (max(4, n+1))
dp[1] = 1
dp[2] = 3
dp[3] = 5
for i in range(4, n+1):
    dp[i] += dp[i-1] + 2*dp[i-2]
    
print(dp[n]%10007)