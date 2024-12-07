# 실행시간: 268 ms
# 메모리: 40644 KB
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/1927
# Reference: priority queue

import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
que = PriorityQueue()
for _ in range(n):
    num = int(input())
    if num == 0:
        if que.empty():
            print(0)
        else:
            print(que.get())
            
    else:
        que.put(num)
    
    