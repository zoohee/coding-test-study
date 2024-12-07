# 실행시간: 656 ms
# 메모리: 74140 KB
# 난이도: Gold 2
# Url: https://www.acmicpc.net/problem/1781
# Reference: 
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

que = []
for i in range(len(arr)):
    heapq.heappush(que, arr[i][1])
    if arr[i][0] < len(que):
        heapq.heappop(que)

print(sum(que))