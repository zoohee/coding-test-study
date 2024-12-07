# 실행시간: 44 ms
# 메모리: 31120 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/1027
# Reference: 

import sys
input = sys.stdin.readline

n = int(input())
bd = list(map(int, input().split()))
answer = [0]*n

for i in range(n-1) :
  max_slope = -float('inf')
  for j in range(i+1, n) :
    slope = (bd[j] - bd[i]) / (j - i)
    
    if slope <= max_slope : continue
  
    max_slope = max(max_slope, slope)
    answer[i] += 1
    answer[j] += 1

print(max(answer))