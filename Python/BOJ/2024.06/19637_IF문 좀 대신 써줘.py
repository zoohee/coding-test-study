# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

titles = []
powers = []
for _ in range(n):
    title, power = input().split()
    titles.append(title)
    powers.append(int(power))

for _ in range(m):
    c = int(input())
    
    right = len(titles)
    left = 0
    result = 0
    
    while left <= right:
        mid = (left+right) // 2
        if powers[mid] >= c:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(titles[result])
    