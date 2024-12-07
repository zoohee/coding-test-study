# 실행시간: 3552 ms
# 메모리: 112564 KB
# 난이도: Gold 3
# Url: https://www.acmicpc.net/problem/10836
# Reference: PyPy3 통과 코드
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
# growth = [list(map(int, input().split())) for _ in range(n)] # 0, 1, 2의 개수
graph = [1] * (2*m-1)

for i in range(n):
    a, b ,c = map(int, input().split())
    for j in range(a, a+b):
        graph[j] += 1
    for j in range(a+b, 2*m-1):
        graph[j] += 2
    
for i in range(m-1, -1, -1):
    print(*([graph[i]] + graph[m:]))