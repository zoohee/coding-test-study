import sys
input = sys.stdin.readline

def REC(n):
    if n < 3:
        return 1
    else:
        return REC(n-1) + REC(n-2)

n = int(input())
print(REC(n))

# 재귀는 거꾸로 생각하셈
# 이 코드 시간초과

# 여기서 base condition은 
# n >= 2 일때만 가능하다는 조건