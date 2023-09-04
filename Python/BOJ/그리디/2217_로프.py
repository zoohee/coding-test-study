# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 4
# Url: https://www.acmicpc.net/problem/2217
# Reference: Me
import sys
input = sys.stdin.readline

N = int(input())
answer = 0
rope=[int(input().strip()) for _ in range(N)]

answer = [max(rope)]
rope.sort(reverse=True)
for i in range(2, N+1):
    answer.append(rope[i-1]*i)

print(max(answer))