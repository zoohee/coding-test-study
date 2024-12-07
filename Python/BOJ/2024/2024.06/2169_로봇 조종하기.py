# 실행시간: 1428 ms
# 메모리: 70972 KB
# 난이도: Gold 2
# Url: https://www.acmicpc.net/problem/2169
# Reference: 
import sys
from collections import deque
input = sys.stdin.readline
    
n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

for j in range(1, m):
    dp[0][j] += dp[0][j-1]

for i in range(1, n):
    left_to_right = dp[i][:] # 왼쪽에서 오른쪽으로 가는 경우
    right_to_left = dp[i][:] # 오른쪽에서 왼쪽으로 가는 경우
    
    for j in range(m):
        if (j == 0):
            left_to_right[j] += dp[i-1][j]
        else:
            left_to_right[j] += max(dp[i-1][j], left_to_right[j-1])
            
    for j in range(m-1, -1, -1):
        if (j == m-1):
            right_to_left[j] += dp[i-1][j]
        else:
            right_to_left[j] += max(dp[i-1][j], right_to_left[j+1])

    for j in range(m):
        dp[i][j] = max(left_to_right[j], right_to_left[j])

print(dp[n-1][m-1])


