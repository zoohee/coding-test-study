# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

max_book = 0
pos = []
neg = []
for b in books:
    max_book = max(abs(b), max_book)
    if b > 0:
        pos.append(b)
    else:
        neg.append(abs(b))
        
pos.sort(reverse=True)
neg.sort(reverse=True)

answer = 0
for i in range(0, len(pos), m):
    answer += pos[i]*2

for i in range(0, len(neg), m):
    answer += neg[i]*2

print(answer - max_book)