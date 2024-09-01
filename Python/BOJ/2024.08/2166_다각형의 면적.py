# 실행시간: 40 ms
# 메모리: 32140 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/2166
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
pos = [tuple(map(int, input().split())) for _ in range(n)]
pos.append(pos[0])

answer = 0
for i in range(n):
    answer += pos[i][0] * pos[i+1][1] - pos[i+1][0] * pos[i][1]

print(abs(answer)/2)
