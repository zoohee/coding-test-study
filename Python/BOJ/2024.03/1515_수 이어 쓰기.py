# 실행시간: 52ms
# 메모리: 31120KB
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/1515
# Reference: https://velog.io/@cria2000/%EB%B0%B1%EC%A4%80-1515-%EC%88%98-%EC%9D%B4%EC%96%B4-%EC%93%B0%EA%B8%B0python
import sys
input = sys.stdin.readline
nums = input().rstrip()

n = 0
idx = 0
while True:
    n += 1
    for s in str(n):
        if nums[idx] == s:
            idx += 1
            if idx >= len(nums):
                print(n)
                exit()