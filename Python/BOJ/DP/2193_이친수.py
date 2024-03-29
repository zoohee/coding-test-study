# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/2193
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
dp = [1, 1]
for i in range(2, n):
    dp.append(dp[i-2] + dp[i-1])
print(dp[n-1])

# 피보나치 아닌 풀이.. -> 메모리 초과
# n = int(input())
# dp = [[] for _ in range(n)]

# dp[0] = "1"
# if n == 1:
#     print("1")
#     exit(0)
    
# for i in range(1, n):
#     for j in range(len(dp[i-1])):
#         if dp[i-1][j][-1] == "1":
#             dp[i].append(dp[i-1][j]+"0")
#         else:
#             dp[i].append(dp[i-1][j]+"0")
#             dp[i].append(dp[i-1][j]+"1")

# print(len(dp[-1]))