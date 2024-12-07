# 실행시간: 72 ms
# 메모리: 31120 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/9084
# Reference: 

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    money = int(input())
    
    dp = [0] * (money+1)
    dp[0] = 1
    for coin in arr:
        for i in range(1, money+1):
            if i >= coin:
                dp[i] += dp[i-coin]            
                
    print(dp[money])