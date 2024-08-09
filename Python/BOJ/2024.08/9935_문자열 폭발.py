# 실행시간: 484 ms
# 메모리: 41268 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/9935
# Reference: https://kjimin0619.tistory.com/61
import sys
input = sys.stdin.readline

def solve():
    a = input().rstrip()
    b = input().rstrip()
    bomb_size = len(b)

    stack = []
    for i in a:
        stack.append(i)
        if len(stack) >= bomb_size and stack[-bomb_size:] == list(b):
            for _ in range(bomb_size):
                stack.pop()

    return ''.join(stack) if stack else "FRULA"

print(solve())