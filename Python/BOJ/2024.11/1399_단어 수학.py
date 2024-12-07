# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

N = int(input())
words = [list(input().rstrip()) for _ in range(N)]
words.sort(key = lambda x: -len(x))

dic = {}
for word in words:
    x = len(word) - 1
    for w in word:
        if w in dic:
            dic[w] += 10**x
        else:
            dic[w] = 10**x
        x -= 1

dic_sort = sorted(dic.values(), reverse=True)
result = 0
num = 9
for k in dic_sort:
    result += k * num
    num -= 1
print(result)    
