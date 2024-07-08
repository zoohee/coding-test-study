import sys
input = sys.stdin.readline
from collections import deque

d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = deque(list(map(int, input().split())))

# 반지름 작은걸로 다시 정렬
# 5 6 4 3 6 2 3 -> 5 5 4 3 3 2 2
for i in range(d-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]
 
# 피자는 첫번째, 오븐은 밑에서부터 확인
cur = 0
for i in range(d-1, -1, -1):
    # 현 피자 반지름이 오븐보다 크면 넘어가기
    if pizza[cur] > oven[i]:
        continue
    
    # 오븐에 못넣게 되면 다음 피자 탐색
    cur += 1
    # 오븐에 피자 다 넣으면 종료
    if cur >= n:
        print(i+1)
        sys.exit(0)

print(0)