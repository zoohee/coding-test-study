# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/1182
# Reference: 
import sys
input = sys.stdin.readline

def subset_sum(start):
    global cnt
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