# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/2179
# Reference: 

import sys
input = sys.stdin.readline

n = int(input())
word = list(input().rstrip())
words = [input().rstrip() for _ in range(n-1)]

answer = 0
for i in range(len(words)):
    cmp = word[:]
    cnt = 0
    
    for w in words[i]:
        if w in cmp:
            cmp.remove(w)
        else:
            cnt += 1
    
    if cnt<2 and len(cmp)<2:
        answer += 1
        
print(answer)