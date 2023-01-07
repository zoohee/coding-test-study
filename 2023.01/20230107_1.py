#3273
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
x = int(input())
cnt = 0

i = 0
j = n - 1

li.sort()

while i < j:
    tmp = li[i]+li[j]
    if tmp == x:
        cnt += 1
        i += 1
        j -= 1
    # x보다 작으면 작은값 인덱스 늘려주기
    elif tmp < x:
        i += 1
    else:
        j -= 1
    print(tmp)
    print(li)
        
print(cnt)   