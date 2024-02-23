# 실행시간: ms
# 메모리: KB
# 난이도: Bronze 1
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

words = input().rstrip()

dict = {chr(ord('A')+n): 0 for n in range(26)}

for word in words:
    word = word.upper()
    dict[word] += 1

# 여기서 최대값이 여러개인것만 걸러내기
max_value = max(dict.values())
ans = 0
key = ""
for i in range(26):
    if max_value:
        ans += 1
        key = list(dict.keys())[i]

    if ans > 1:
        print("?")
        exit(0)

if ans == 1:
    print(key)
    
    
