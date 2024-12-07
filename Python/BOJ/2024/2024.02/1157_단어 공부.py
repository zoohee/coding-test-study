# 실행시간: 288ms
# 메모리: 33076KB
# 난이도: Bronze 1
# Url: https://www.acmicpc.net/problem/1157
# Reference: me
import sys
input = sys.stdin.readline

words = input().rstrip()

dict = {chr(ord('A')+n): 0 for n in range(26)}

for word in words:
    word = word.upper()
    dict[word] += 1

max_value = max(dict.values())
ans = 0
key = ""
for k in dict.keys():
    if max_value == dict.get(k):
        ans += 1
        key = k

    if ans > 1:
        print("?")
        exit(0)

if ans == 1:
    print(key)
    
    
