# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/11659
# Reference: 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

for i in range(1, n):
    num[i] += num[i-1]

num = [0] + num

for i in range(m):
    a, b = map(int, input().split())
    print(num[b] - num[a-1])