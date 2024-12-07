# 실행시간: 44 ms
# 메모리: 33164 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/1911
# Reference: 
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[0], x[1]))
# l: 널빤지 크기
cnt = 0
cur = arr[0][0]
for s, e in arr:
    if cur > e:
        continue
    
    if cur < s:
        cur = s
    
    dist = e - cur
    r = 0 if dist % l == 0 else 1
    
    cur += (dist//l + r) * l # 널빤지 크기만큼 더해줌
    cnt += dist//l + r

print(cnt)
    
