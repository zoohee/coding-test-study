import sys
input = sys.stdin.readline

n, k = map(int, input().split())
backpack = [list(map(int, input().split())) for _ in range(n)]
zero = [[0, 0]]
bp = zero + backpack

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for w in range(k+1):
        if bp[i][0] > w: # 못넣는 상황
            dp[i][w] = dp[i-1][w] 
        else: # 넣는 상황
            dp[i][w] = max(bp[i][1] + dp[i-1][w - bp[i][0]], dp[i-1][w])

print(dp[n][k])
