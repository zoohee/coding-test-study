# 실행시간: 216 ms
# 메모리: 31120 KB
# 난이도: Gold 3
# Url: https://www.acmicpc.net/problem/14658
# Reference: https://velog.io/@cria2000/%EB%B0%B1%EC%A4%80-14658-%ED%95%98%EB%8A%98%EC%97%90%EC%84%9C-%EB%B3%84%EB%98%A5%EB%B3%84%EC%9D%B4-%EB%B9%97%EB%B0%9C%EC%B9%9C%EB%8B%A4python
import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(k)]
ans = 0

for x, y in pos:
    for sx, sy in pos:
        cnt = 0
        for px, py in pos:
            if x <= px <= x+l and sy <= py <= sy+l:
                cnt += 1
        ans = max(ans, cnt)

print(k - ans)
    