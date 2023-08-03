# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 1
# Url: https://www.acmicpc.net/problem/13335
# Reference: 
import sys
input = sys.stdin.readline
from collections import deque

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
bridge = [0] * w
time = 0

while bridge:
    time += 1
    bridge.pop(0) # 0번째 탈출
    if truck:
        if sum(bridge) + truck[0] <= L: # 최대 무게 안 넘으면
            bridge.append(truck.pop(0))
        else: # 넘으면 0 추가
            bridge.append(0) 

print(time)
