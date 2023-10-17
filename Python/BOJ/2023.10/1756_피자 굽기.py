import sys
input = sys.stdin.readline
from collections import deque

d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = deque(list(map(int, input().split())))
index = len(oven)-1

while pizza and oven:
    cur_p = pizza.popleft()
    for i in range(index, 0, -1):
        if cur_p <= oven[i]:
            continue
        else:
            index = i-1
            break

if pizza:
    print(0)
else:
    print(index)