# 실행시간: ms
# 메모리: KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/25556
# Reference: 

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = [[] for _ in range(4)]
mark = False
for i in range(len(arr)):
    for j in range(4):
        if len(stack[j]) == 0:
            stack[j].append(arr[i])
            mark = False
            break
        
        if stack[j][-1] < arr[i]:
            stack[j].append(arr[i])
            mark = False
            break
        
        else:
            mark = True

if mark:
    print("NO")
else:
    print("YES")