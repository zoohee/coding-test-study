# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/2293
# Reference: https://zu-techlog.tistory.com/48
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_value = [ int(input().rstrip()) for _ in range(n)]
dp = [ k+1 for _ in range(k+1)]
dp[0] = 1

for coin in coin_value:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]
        
print(dp[k])