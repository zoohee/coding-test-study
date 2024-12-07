# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/2294
# Reference: 
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_value = [ int(input().rstrip()) for _ in range(n)]
dp = [ k+1 for _ in range(k+1)]
dp[0] = 0

for coin in coin_value:
    # 해당 코인의 가치부터 만들 수 있음
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
        
if dp[k] == k+1:
    print(-1)
else:
    print(dp[k])