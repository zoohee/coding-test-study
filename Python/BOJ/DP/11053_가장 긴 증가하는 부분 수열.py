import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
seq = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            seq[i] = max(seq[j] + 1, seq[i])

print(max(seq))