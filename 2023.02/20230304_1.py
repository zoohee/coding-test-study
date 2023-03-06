import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = deque()

for i in range(n):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

# n = int(input())

# a_queue = []

# for i in range(n):
#     a_queue.append(i+1)
    
# while len(a_queue)>1:
#     a_queue.pop(0)
#     a_queue.append(a_queue.pop(0))
    
# print(a_queue[0])
