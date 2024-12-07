# 실행시간: 60ms
# 메모리: 32140KB
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/2512
# Reference: https://deep-learning-study.tistory.com/604
import sys
input = sys.stdin.readline

n = int(input())
regions = list(map(int, input().split()))
m = int(input())

left, right = 0, max(regions)
while left <= right:
    mid = (left + right) // 2
    total = 0
    for r in regions:
        if r > mid:
            total += mid
        else:
            total += r
    if total <= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)
