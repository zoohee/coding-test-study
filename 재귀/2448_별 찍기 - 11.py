# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

def REF(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    stars = REF(n//2)
    arr = []
    for star in stars:
        arr.append(' '*((n//2))+star)
    for star in stars:
        arr.append(star+' '*(n//2 - 2)+star)
    for star in stars:
        arr.append(star)
    return arr

n = int(input())
print(*REF(n), sep='\n')