# 실행시간: 96ms
# 메모리: 34044KB
# 난이도: Silver 5
# Url: https://www.acmicpc.net/problem/10431
# Reference: me
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for i in range(n):
    str = list(map(int, input().split()))
    t = str[0]
    height = str[1:len(str)]
    new_arr = [height[0]]
    
    cnt = 0
    for j in range(1, 20):
        length = len(new_arr)
        inserted = False
        for k in range(length-1, -1, -1):
            if height[j] < new_arr[k]:
                cnt += 1
            else:
                tmp = new_arr[k+1:length]
                new_arr = new_arr[:k+1]
                new_arr.append(height[j])
                new_arr = new_arr + tmp
                inserted = True
                break

        if not inserted:
            if height[j] <= new_arr[0]:
                new_arr = [height[j]] + new_arr
            else:
                new_arr = new_arr + [height[j]]

    print(t, cnt)

                 
