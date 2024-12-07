# 실행시간: 108 ms
# 메모리: 41180 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/20159
# Reference: 

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

origin_sum = 0
for i in range(n):
    if i % 2 == 0:
        origin_sum += arr[i]
answer = origin_sum

tmp = origin_sum
for i in range(n-1, 0, -2): # 정훈 차례
    tmp += arr[i]
    tmp -= arr[i-1]
    answer = max(answer, tmp)

tmp = origin_sum
for i in range(n-2, 1, -2):
    tmp -= arr[i]
    tmp += arr[i-1]
    answer = max(answer, tmp)

print(answer)