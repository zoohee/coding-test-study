# 실행시간: 32 ms
# 메모리: 31120 KB
# 난이도: Gold 3
# Url: https://www.acmicpc.net/problem/14725
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    tmp = list(input().split())
    arr.append(tmp[1:])
arr.sort()

answer = []
for i in range(n):
    if i == 0:
        for j in range(len(arr[i])):
            answer.append('--'*j + arr[i][j])
    else:
        idx = 0 # 이전 리스트와 비교해서 겹치는 원소 개수 저장
        for j in range(len(arr[i])):
            if arr[i-1][j] != arr[i][j] or len(arr[i-1]) <= j:
                break
            else:
                idx = j+1
        for j in range(idx, len(arr[i])):
            answer.append('--'*j + arr[i][j])

for a in answer:
    print(a)