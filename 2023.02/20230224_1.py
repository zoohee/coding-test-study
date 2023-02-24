import sys
input = sys.stdin.readline

cursor = 0
pw = []
n = int(input())

for i in range(n):
    str = list(input())
    for j in range(len(str)):
        if str[j] == '<':
            if cursor > 0:
                cursor -= 1
        elif str[j] == '>':
            if cursor < len(pw):
                cursor += 1
        elif str[j] == '-':
            if cursor > 0:
                pw.remove(pw[cursor-1])
                cursor -= 1
        else:
            pw.insert(cursor, str[j])
            cursor += 1
    pw.remove('\n')
    print(''.join(pw))
    pw = []         