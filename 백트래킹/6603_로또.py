# 시간복잡도: 순열 같은 경우 2^n 
# 최악시간: 
# 난이도: Silver 2
# Url: https://www.acmicpc.net/problem/6603
# Reference: 
import sys
input = sys.stdin.readline

s = []
def lotto(start):
    if len(s) == 6:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, len(arr)):
        s.append(arr[i])
        lotto(i+1)
        s.pop()
    
while(True):
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    lotto(0)
    print("")
