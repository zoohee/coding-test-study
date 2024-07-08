# 1021
# 회전하는 큐
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
deq = deque([i for i in range(1, n+1)])
num_list = list(map(int,input().split()))
cnt = 0

