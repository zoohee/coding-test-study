import sys
input = sys.stdin.readline

list = [0] * 9

for i in range(9):
    list[i] = int(input())

max_num = max(list)
print(max_num)

for i in range(9):
    if max_num == list[i]:
        print(i)
        break