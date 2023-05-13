#10808
import sys
input = sys.stdin.readline

s = input()
list = [0] * 26
# ord() 문자를 숫자로 바꿔줌

for i in range(len(s)-1):
    list[ord(s[i])-97] += 1

for i in range(len(list)):
    print(list[i], end=" ")
