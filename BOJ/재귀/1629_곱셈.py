from collections import deque
import sys
input = sys.stdin.readline

def REC(a, b):
    if b == 1:
        return a % c
    elif b % 2 == 0: # b가 짝수
        return (REC(a, b//2))**2 % c
    else: # b가 홀수
        return (REC(a, b//2))**2 * a % c
    
a, b, c = map(int, input().split())

print(REC(a, b))
