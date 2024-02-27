# 실행시간: 44ms
# 메모리: 31120KB
# 난이도: Silver 5
# Url: https://www.acmicpc.net/problem/4569
# Reference: me
import sys
input = sys.stdin.readline

m = ['a', 'e', 'i', 'o', 'u']

def check(password):
    
    if len(password) == 1:
        if password[0] in m:
            return True
        else:
            return False
        
    repeat = 1
    moeum = 0
    if password[0] in m:
        moeum += 1
    for i in range(1, len(password)):
        if password[i] in m:
            moeum += 1
        # 3. 같은 글자가 연속적으로 두번 오면 안 됨
        if password[i-1] == password[i]:
            if password[i] != 'e' and password[i] != 'o':
                return False
            
        if password[i-1] in m and password[i] in m:
            repeat += 1
        elif password[i-1] not in m and password[i] not in m:
            repeat += 1
        else:
            repeat = 1
            
        # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        if repeat == 3:
            return False
        
    # 1. 모음이 하나 반드시 포함    
    if moeum > 0:
        return True
    else:
        return False
            
while(True):
    p = input().rstrip()
    
    if p == "end":
        exit(0)
    else:
        if check(p):
            print("<%s> is acceptable." % p)
        else:
            print("<%s> is not acceptable." % p)