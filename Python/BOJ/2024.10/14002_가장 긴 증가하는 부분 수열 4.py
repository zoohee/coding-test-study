# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    m = 0
    for j in range(0, i): # 나보다 작은 애들만
        if arr[i] > arr[j]:
            m = max(m, dp[j])
    dp[i] = m+1

x = max(dp)
print(x)

tmp = x
result = []
for i in range(n, -1, -1):
    if dp[i] == tmp:
        result.append(arr[i])
        tmp -= 1
        
result.sort()
for i in range(1, len(result)):
    print(result[i], end=" ")