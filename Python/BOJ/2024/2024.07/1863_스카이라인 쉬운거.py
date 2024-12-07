# 실행시간: 52 ms
# 메모리: 31120 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/1863
# Reference: 
import sys
input = sys.stdin.readline

n = (int(input()))

stack = []
answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    
    while len(stack) > 0 and stack[-1] > y:
        answer += 1
        stack.pop()
    
    # y가 같은 부분 제외
    if len(stack) > 0 and stack[-1] == y:
        continue
    
    stack.append(y)

while len(stack) > 0:
    if stack[-1] > 0:
        answer += 1
    stack.pop()
    
print(answer)