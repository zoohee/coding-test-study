#11328
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = list(input().split())
    print(sorted(a))
    print(sorted(b))
    if sorted(a) == sorted(b) :
        print("Possible")
    else:
        print("Impossible")