# 실행시간: 1016 ms
# 메모리: 53648 KB
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/22233
# Reference: me

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = {}
for _ in range(n):
    keywords[input().rstrip()] = 0    

for _ in range(m):
    article = list(input().rstrip().split(','))
    for a in article:
        if a in keywords.keys():
            del keywords[a]
    print(len(keywords))