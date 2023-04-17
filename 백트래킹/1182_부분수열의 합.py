# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/1182
# Reference: https://great-park.tistory.com/37
import sys
input = sys.stdin.readline

def subset_sum(start):
    global cnt
    # 합이 S와 같고 리스트에 값이 있으면 카운트
    if sum(answer) == S and len(answer) > 0:
        cnt += 1
        
    for i in range(start, N):
        answer.append(arr[i])
        subset_sum(i+1)
        answer.pop()
    
N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
cnt = 0
subset_sum(0)
print(cnt)