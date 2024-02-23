# 실행시간: 40ms
# 메모리: 31120KB
# 난이도: Bronze 3
# Url: https://www.acmicpc.net/problem/5073
# Reference: me
import sys
input = sys.stdin.readline

def triangle(a, b, c):
    if a+b<=c or a+c<=b or b+c<=a:
        return False
    else:
        return True

while(True):
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break 
    if a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        if triangle(a, b, c):
            print("Isosceles")
        else:
            print("Invalid")
    else:
        if triangle(a, b, c):
            print("Scalene")
        else:
            print("Invalid")