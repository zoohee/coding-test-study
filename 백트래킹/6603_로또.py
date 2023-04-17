# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

s = []
def lotto( depth):
    if len(s) == 6:
        print(' '.join(map(str,s)))
        return
    
    for i in range(depth, len(arr)):
        if len(s) == 0:
            s.append(arr[i])
            lotto(depth+1)
            s.pop()
        else:
            if s[-1] < arr[i]:
                s.append(arr[i])
                lotto( depth+1)
                s.pop()
        

    
while(True):
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    lotto(0)
    print("")
