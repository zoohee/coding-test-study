# 실행시간: 40ms
# 메모리: 31120KB
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/20310
# Reference: me
import sys
input = sys.stdin.readline

s = list(input())
zero = s.count('0') // 2
one =  s.count('1') // 2

check = 0
for i in s:
    if check == one:
        break
    if i == '1':
        s.remove(i)
        check += 1

check = 0
s = s[::-1]
for i in s:
    if check == zero:
        break
    if i == '0':
        s.remove(i)
        check += 1

for i in s[::-1]:
    print(i, end='')
    
        
        
