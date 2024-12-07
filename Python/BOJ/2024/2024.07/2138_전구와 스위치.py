# 실행시간: 120 ms
# 메모리: 33468 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/2138
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
light = list(map(int, input().strip()))
want = list(map(int, input().strip()))

def sol(cnt):
    tmp = light.copy()
    for i in range(1, n):
        if tmp[i-1] != want[i-1]:
            tmp[i-1] = int(not tmp[i-1])
            tmp[i] = int(not tmp[i])
            if i != n-1:
                tmp[i+1] = int(not tmp[i+1])
            cnt += 1
    if tmp != want:
        cnt = -1
    return cnt
    
a = sol(0)
light[0] = int(not light[0])
light[1] = int(not light[1])
b = sol(1)

if a == -1:
    print(b)
elif b == -1:
    print(a)
else:
    print(min(a, b))