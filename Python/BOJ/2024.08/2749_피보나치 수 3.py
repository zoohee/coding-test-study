# 실행시간: 504 ms
# 메모리: 89968 KB
# 난이도: Gold 2
# Url: https://www.acmicpc.net/problem/2749
# Reference: https://kyun2da.github.io/2020/08/30/fibonacci/
import sys
input = sys.stdin.readline

n = int(input())

mod = 1000000
fibo = [0, 1]
p = mod//10*15

for i in range(2,p):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= mod

print(fibo[n % p])