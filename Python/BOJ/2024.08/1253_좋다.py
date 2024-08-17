# 실행시간: 1196 ms
# 메모리: 31120 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
for i in range(n):
    num = arr[i]
    start = 0
    end = len(arr)-1
    while start < end:
        if arr[start] + arr[end] == num:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif arr[start] + arr[end] > num:
            end -= 1
        elif arr[start] + arr[end] < num:
            start += 1

print(cnt)
            