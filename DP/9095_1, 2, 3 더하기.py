# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/9095
# Reference: https://yongku.tistory.com/1273
import sys
input = sys.stdin.readline

def DP(n):
    # n이 4 이하로 들어오면 IndexError
    d = [0] * (max(4, n+1))
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    return d[n]
    
    
t = int(input())
num_list = [int(input()) for _ in range(t)]
for i in range(t):
    print(DP(num_list[i]))
