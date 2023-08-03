#1697
#숨바꼭질
from collections import deque
import sys
input = sys.stdin.readline

def BFS(n):
    queue = deque()
    queue.append(n)
    
    while(queue):
        s = queue.popleft()
        if s == k:
           return array[s] 
        for next in (s-1, s+1, s*2):
            if 0 <= next < max and not array[next]:
                array[next] = array[s] + 1
                queue.append(next)

max = 100001
n, k = map(int, input().split())
array = [0] * max

print(BFS(n))                