# 실행시간: 36 ms
# 메모리: 31120 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/14719
# Reference: https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-14719%EB%B2%88-%EB%B9%97%EB%AC%BC-python-%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98-%EA%B3%A8%EB%93%9C-5
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

for i in range(1, w-1):
    left = max(block[:i])
    right = max(block[i+1:])
    m = min(left, right)
    if m > block[i]:
        answer += m - block[i]

print(answer)
