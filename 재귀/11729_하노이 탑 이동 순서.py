from collections import deque
import sys
input = sys.stdin.readline

def REC(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    # 6-start-end는 남는 막대의 번호
    REC(n-1, start, 6-start-end)
    print(start, end)
    REC(n-1, 6-start-end, end)
    
n = int(input())
print(2**n-1)
REC(n, 1, 3)