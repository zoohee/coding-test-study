# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 1
# Url: https://www.acmicpc.net/problem/1932
# Reference: Me
import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0: # 첫번째 원소는 오른쪽 대각선만 더하기
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif j == len(triangle[i])-1: # 마지막 원소는 왼쪽 대각선만 더하기
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else: # 가운데 원소는 양쪽 대각선 중 큰 값 더하기
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[n-1]))
