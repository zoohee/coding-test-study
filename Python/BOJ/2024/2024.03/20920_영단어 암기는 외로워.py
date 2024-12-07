# 실행시간: 312ms
# 메모리: 54644KB
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/20920
# Reference: me
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words = {}
for i in range(n):
    w = input().rstrip()
    if len(w) < m:
        continue
    if w not in words:
        words[w] = 1
    else:
        words[w] += 1
        
sorted_count = sorted(words, key = lambda x: (-words[x], -len(x), x))

for i in range(len(sorted_count)):
    print(sorted_count[i])