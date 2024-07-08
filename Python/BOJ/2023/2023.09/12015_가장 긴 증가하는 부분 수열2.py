import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]

for i in range(1, len(arr)):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        left = 0
        right = len(lis)-1
        while left<right:
            mid = (right+left)//2
            if lis[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid
        lis[right] = arr[i]

print(len(lis))