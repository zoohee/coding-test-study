from collections import deque
import sys
input = sys.stdin.readline

cnt = 0
def REC(n, a, b):
    global cnt
    if a == r and b == c:
        print(int(cnt))
        exit(0)
    
    if n == 1:
        cnt += 1
        return 
    
    if not (a <= r < a + n and b <= c < b + n):
        cnt += n * n
        return
    
    REC(n/2, a, b) # 1사분면
    REC(n/2, a, b+n/2) # 2사분면
    REC(n/2, a+n/2, b) # 3사분면
    REC(n/2, a+n/2, b+n/2) # 4사분면
    
n, r, c = map(int, input().split())
REC(2 ** n, 0, 0)