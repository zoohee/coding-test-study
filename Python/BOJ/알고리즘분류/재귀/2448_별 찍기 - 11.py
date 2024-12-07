# 시간복잡도: 
# 최악시간: 
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/2448
# Reference: 
import sys
input = sys.stdin.readline

def REF(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    stars = REF(n//2)
    arr = []
    for star in stars:
        arr.append(' '*(n//2)+star+' '*(n//2))
    for star in stars:
        arr.append(star+' '+star)
    return arr

n = int(input())
print("\n".join(REF(n)))