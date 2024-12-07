# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

l = 0
r = n-1

answer = abs(arr[l] + arr[r])
left = l
right = r
while l < r:
    tmp = arr[l] + arr[r]
    
    if abs(tmp) <= answer:
        left = l
        right = r
        answer = abs(tmp)
        
        if answer == 0:
            break
    
    if tmp < 0:
        l += 1
    else:
        r -= 1

print(arr[left] + arr[right])