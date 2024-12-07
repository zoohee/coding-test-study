# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
travel = [list(map(int, input().split())) for _ in range(n)]
dp = [[601]*m for _ in range(n)]

for i in range(m):
    dp[0][i] = travel[0][i]

direction = [2 for _ in range(m)]
# 내려 가면서 작은 값 저장
for i in range(1, n):
    for j in range(m):
        if j == 0:
            if dp[i-1][j] < dp[i-1][j+1] and direction[j] != 0:
                dp[i][j] = travel[i][j] + dp[i-1][j]
                direction[0] = 0
            elif direction[j] != 1:
                dp[i][j] = travel[i][j] + dp[i-1][j+1]
                direction[0] = 1
        elif j == m-1:
            if dp[i-1][j-1] < dp[i-1][j] and direction[j] != -1:
                dp[i][j] = travel[i][j] + dp[i-1][j-1]
                direction[j] = -1
            elif direction[j] != 0:
                dp[i][j] = travel[i][j] + dp[i-1][j]
                direction[j] = 0
        else:
            arr = [dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]]
            arr.sort()
            check = False
            for k in range(3):
                for l in range(3):
                    if arr[k] == dp[i-1][j-1+l] and direction[j] != l-1:
                        dp[i][j] = travel[i][j] + arr[k]
                        direction[j] = l-1
                        check = True
                        break
                if check:
                    break
    print(direction)

print("=============")
for i in range(n):
    for j in range(m):
        print(dp[i][j], end=" ")
    print()

print(min(dp[n-1]))

# 4 2
# 19 71 
# 9 100 
# 12 77 
# 75 51 