# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/12852
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
d = [i for i in range(n+1)]
d[1] = 0
method = [i for i in range(n+1)]
method[1] = 0

for i in range(2, n+1):
    d[i] = d[i-1] + 1 
    method[i] = i-1
    if i%3 == 0 and d[i] > d[i//3]+1:
        d[i] = d[i//3] + 1
        method[i] = i//3
    if i%2 == 0 and d[i] > d[i//2]+1:
        d[i] = d[i//2] + 1 
        method[i] = i//2
    
print(d[n])
print(n, end=" ")

order_num = n
while method[order_num] != 0:
    print(method[order_num], end=" ")
    order_num = method[order_num]