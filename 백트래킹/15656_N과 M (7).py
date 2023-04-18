# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/15655
# Reference: 
import sys
input = sys.stdin.readline

s = []
def sequence(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(len(arr)):
        s.append(arr[i])
        sequence(i)
        s.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sequence(0)