# 실행시간: 36 ms
# 메모리: 32140 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/2212
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()

dist = [arr[i+1]-arr[i] for i in range(n-1)]
dist.sort()

print(sum(dist[:n-k]))