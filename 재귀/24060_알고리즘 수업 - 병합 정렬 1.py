import sys
input = sys.stdin.readline

def merge_sort(L):
    if len(L) == 1:
        return L
    
    mid = (len(L)+1)//2
    
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    
    i, j = 0, 0
    tmp = []
    
    while i<len(left) and j<len(right):
        if left[i] < right[i]:
            tmp.append(left[i])
            answer.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            answer.append(right[j])
            j += 1
    
    while i<len(left):
        tmp.append(left[i])
        answer.append(left[i])
        i += 1
    
    while j<len(right):
        tmp.append(right[j])
        answer.append(right[j])
        j += 1
        
    return tmp

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
merge_sort(arr)

if len(answer) < k:
    print(-1)
else:
    print(answer[k-1])