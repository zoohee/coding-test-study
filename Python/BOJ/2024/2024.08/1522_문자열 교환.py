# 실행시간: 36 ms
# 메모리: 31120 KB
# 난이도: Silver 1
# Url: https://www.acmicpc.net/problem/1522
# Reference: me
import sys
input = sys.stdin.readline

s = input().rstrip()
a = s.count('a')
s += s[0:a-1]

min_cnt = sys.maxsize
for i in range(len(s)-a+1):
    min_cnt = min(min_cnt, s[i:i+a].count('b'))
    
print(min_cnt)