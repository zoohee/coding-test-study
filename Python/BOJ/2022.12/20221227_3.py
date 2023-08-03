import sys
input = sys.stdin.readline

num = [int(input()) for _ in range(9)]
one = 0
two = 0

for i in range(9):
    for j in range(i+1, 9):
        if sum(num) - (num[i]+num[j]) == 100 :
            one = num[i]
            two = num[j]
            break

num.remove(one)
num.remove(two)
num.sort()
            
for i in range(7):
    print(num[i])
