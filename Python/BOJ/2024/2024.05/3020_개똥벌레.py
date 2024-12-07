# 실행시간: 236ms
# 메모리: 59140KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/3020
# Reference: https://velog.io/@qazws78941/python%EB%B0%B1%EC%A4%80-3020-%ED%92%80%EC%9D%B4
import sys
input = sys.stdin.readline

n, h = map(int, input().split())
cave = [int(input()) for _ in range(n)]
# 아래>위>아래>위

lines = [0] * h
for i in range(n):
    if i % 2 == 0:
        lines[h-cave[i]] += 1
    else:
        lines[0] += 1
        lines[cave[i]] -= 1

for i in range(1, h):
    lines[i] += lines[i-1]
    
min_ans = min(lines)
cnt = lines.count(min_ans)
print(min_ans, cnt)
