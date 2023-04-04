import sys
input = sys.stdin.readline

def REF(n):
    if n == 3:
        return ['***', '* *', '***']
    stars = REF(n//3)
    arr = []
    for star in stars:
        arr.append(star*3)
    for star in stars:
        arr.append(star+' '*(n//3)+star)
    for star in stars:
        arr.append(star*3)
    return arr

n = int(input())
print(*REF(n), sep='\n')

# https://kkg0.tistory.com/14
# 