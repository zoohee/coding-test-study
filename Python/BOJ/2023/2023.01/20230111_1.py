#11328
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = list(input().split())
    # sorted는 list로 받았을 때 가능하다
    if sorted(a) == sorted(b) :
        print("Possible")
    else:
        print("Impossible")