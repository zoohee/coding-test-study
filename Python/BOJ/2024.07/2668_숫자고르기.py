# 실행시간: 44 ms
# 메모리: 31120 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/2668
# Reference: 

def dfs(vert,start):
    visited[vert] = True
    value = field[vert]
    if not visited[value]:
        dfs(value, start)
    elif visited[value] and value == start: # 사이클이면 답에 추가
        result.append(value)

n = int(input())
field = [0]
result = []
for i in range(n):
    field.append(int(input()))

for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i)

result.sort()
print(result)
print(len(result))
for ele in result:
    print(ele)