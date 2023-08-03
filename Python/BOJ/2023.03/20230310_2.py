#18258
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    order = list(input().split())
    if order[0] == "push":
        queue.append(order[1])
    elif order[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
            
# python의 삼항 연산자 ??      
# def asdf(a, q):
#     if a[0] == 'push':
#         q.append(a[1])
#         return None
#     elif a[0] == 'pop':
#         return q.popleft() if q else '-1'
#     elif a[0] == 'size':
#         return str(len(q))
#     elif a[0] == 'empty':
#         return '0' if q else '1'
#     elif a[0] == 'front':
#         return q[0] if q else '-1'
#     elif a[0] == 'back':
#         return q[-1] if q else '-1'