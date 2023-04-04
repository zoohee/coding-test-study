import sys
input = sys.stdin.readline

def REC(n):
    if n < 3:
        return 1
    else:
        return REC(n-1) + REC(n-2)

n = int(input())
print(REC(n))
