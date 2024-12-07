# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()
arr_max,arr_max_index=0,0

for i in range(n):
    if arr_max<arr[i][1]:
        arr_max=arr[i][1]
        arr_max_index=i 

high_x,high_y=arr[0][0],arr[0][1]
result=0

for i in range(1,arr_max_index+1):
    if high_y<arr[i][1]:
        result+=(arr[i][0]-high_x)*high_y
        high_x,high_y=arr[i][0],arr[i][1]


result+=arr[arr_max_index][1]
high_x,high_y=arr[n-1][0],arr[n-1][1]
for i in range(n-1,arr_max_index-1,-1):
    if high_y<=arr[i][1]:
        result+=(high_x-arr[i][0])*high_y
        high_x,high_y=arr[i][0],arr[i][1]

print(result)