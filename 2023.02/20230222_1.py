import sys
input = sys.stdin.readline

str = list(input())
cursor = len(str)
n = int(input())

for _ in range(n):
    order = list(input().split())
    if order[0] == "L":
        if cursor > 0:
            cursor -= 1
    elif order[0] == "D":
        if cursor < len(str):
            cursor += 1
    elif order[0] == "B":
        if cursor > 0:
            str.remove(str[cursor-1])
            cursor -= 1
    else:
        str.insert(cursor, order[1])
        cursor += 1

if '\n' in str:
    str.remove('\n')
print(''.join(str))
        