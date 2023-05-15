# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/1003
# Reference: 
import sys
input = sys.stdin.readline

t = int(input())

def fibo(n):
    count[0] = [1, 0]
    count[1] = [0, 1]
    for i in range(2, n+1):
        count[i][0] = count[i-1][0] + count[i-2][0]
        count[i][1] = count[i-1][1] + count[i-2][1]
    

num = [ int(input()) for _ in range(t)]
count = [[0, 0] for _ in range(max(2, max(num)+1))]

fibo(max(num))
for n in num:
    print(count[n][0], end=" ")
    print(count[n][1])