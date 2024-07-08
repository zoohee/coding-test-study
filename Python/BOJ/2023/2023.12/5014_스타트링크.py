# 실행시간: 884ms
# 메모리: 41440KB
# 난이도: Silver 1
# Url: https://www.acmicpc.net/problem/5014
# Reference: Me + gpt

import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int,input().split())

if (d==0 and s>g) or (u==0 and s<g):
    print("use the stairs")
    exit(0)
    
if s==g:
    print(0)
    exit(0)
    
visited = [False]*(f+1)
btn = [u, -d]
que = deque()
que.append((s, 0))

while(que):
    cur, cnt = que.popleft()
    visited[cur] = True
    
    for i in range(2):
        n_cur = cur + btn[i]
        
        if n_cur == g:
            print(cnt+1)
            exit(0)
        
        if 0 < n_cur <= f and visited[n_cur]==False:
            que.append((n_cur, cnt+1))  
            visited[n_cur] = True      
            
print("use the stairs")