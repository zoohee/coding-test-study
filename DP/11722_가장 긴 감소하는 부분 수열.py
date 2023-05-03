# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/11722
# Reference: 
import sys
input = sys.stdin.readline


# 1. 증가하면 reset

n = int(input())
arr = list(map(int, input().split()))
seq = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            seq[i] = max(seq[j] + 1, seq[i])

print(max(seq))