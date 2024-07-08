import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_set = list(set(arr))
arr_set.sort()

index = dict()
for i in range(len(arr_set)):
    index[arr_set[i]] = i

for i in range(n):
    print(index[arr[i]], end=" ")
    