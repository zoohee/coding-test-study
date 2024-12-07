# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

arr_sum = set()
for x in arr:
    for y in arr:
        arr_sum.add(x+y)
       
def check(): 
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            if arr[i]-arr[j] in arr_sum:
                return arr[i]

print(check())