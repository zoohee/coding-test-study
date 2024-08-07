# 실행시간: 332 ms
# 메모리: 435996 KB
# 난이도: Gold 3
# Url: https://www.acmicpc.net/problem/22866
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
bd = list(map(int, input().split()))

bd_cnt = [0] * n
bd_near = [sys.maxsize] * n
left_stack = []

# 왼->오 돌면서 현재 빌딩 높이보다 낮으면 제거
for i, height in enumerate(bd):
    while left_stack and bd[left_stack[-1]] <= height:
        left_stack.pop()
    
    bd_cnt[i] += len(left_stack)
    
    if left_stack:
        if abs(i-left_stack[-1]) < abs(bd_near[i] - i):
            bd_near[i] = left_stack[-1]
    
    left_stack.append(i)

# 오->왼 돌면서 현재 빌딩 높이보다 큰 빌딩 담기
right_stack = []
for i in range(n - 1, -1, -1):
    height = bd[i]
    
    # 스택에 요소들이 있고 현재 높이보다 낮은 빌딩들은 모두 제거
    while right_stack and bd[right_stack[-1]] <= height:
        right_stack.pop()

    bd_cnt[i] += len(right_stack)

    # 가장 가까이에 있는 빌딩 갱신
    if right_stack:
        if abs(i - right_stack[-1]) < abs(bd_near[i] - i):
            bd_near[i] = right_stack[-1]

    right_stack.append(i)
    
for i in range(n):
    if bd_cnt[i]:
        print(bd_cnt[i], bd_near[i]+1)
    else:
        print(0)