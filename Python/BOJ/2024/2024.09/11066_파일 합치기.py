# 실행시간: 1140 ms
# 메모리: 122024 KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/11066
# Reference: PyPy3 통과
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[0]*k for _ in range(k)]

    for i in range(k-1):
        dp[i][i+1] = arr[i] + arr[i+1]
        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + arr[j]
    
    for n in range(2, k):
        for i in range(k-n):
            j = i + n
            costs = [dp[i][x] + dp[x+1][j] for x in range(i, j)]
            dp[i][j] += min(costs)
    
    print(dp[0][k-1])