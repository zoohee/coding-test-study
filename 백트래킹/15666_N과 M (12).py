# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/15665
# Reference: 
import sys
input = sys.stdin.readline

s = []
def sequence(start):
    global visited
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    check = 0
    for i in range(start, len(arr)):
        if arr[i] != check:
            s.append(arr[i])
            check = arr[i]
            sequence(i)
            s.pop()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
sequence(0)