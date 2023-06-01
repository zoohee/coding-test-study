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
bridge = deque()

answer = 0
cnt = 0 # 마지막 위치 기억해주기
for i in range(n):
    if sum(bridge)+truck[i] <= L and len(bridge) < w:
        bridge.append(truck[i])
        answer += 1
        cnt += 1
    else:
        if sum(bridge)+truck[i] > L:    
            while(True):
                if sum(bridge)+truck[i] <= L:
                    break
                bridge.popleft()
            answer += w-cnt+1
            cnt = w-cnt+1
        else:
            while(True):
                if len(bridge) < w:
                    break
                bridge.popleft()
                # answer += 1
            answer += cnt
        bridge.append(truck[i])
        cnt += 1
    # print(answer)

while(len(bridge)==0):
    bridge.popleft()
    answer += 1
    
# answer += cnt
print(answer)
