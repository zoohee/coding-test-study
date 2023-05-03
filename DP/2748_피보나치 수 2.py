# 시간복잡도: 
# 최악시간: 
# 난이도: Bronze 1
# Url: https://www.acmicpc.net/problem/2748
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
num = 0
seq = [0] * (n+1)

def fibo(n):
    seq[1] = 1
    for i in range(2, n+1):
        seq[i] = seq[i-1] + seq[i-2]

fibo(n)
print(seq[n])
