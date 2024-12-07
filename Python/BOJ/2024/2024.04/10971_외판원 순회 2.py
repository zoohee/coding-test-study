# 실행시간: 136ms
# 메모리: 31120KB
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/10971
# Reference: https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-10971%EB%B2%88-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-2python
import sys
input = sys.stdin.readline

def dfs(start, now, cost, cnt):
    global ans
    if cnt == n:
        if arr[now][start]:
            cost += arr[now][start]
            if ans > cost:
                ans = cost
        return
    
    if cost > ans:
        return

    for i in range(n):
        if not visited[i] and arr[now][i]:
            visited[i] = True
            dfs(start, i, cost + arr[now][i], cnt+1)
            visited[i] = False
    
    

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

ans = sys.maxsize
for i in range(n):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(ans)