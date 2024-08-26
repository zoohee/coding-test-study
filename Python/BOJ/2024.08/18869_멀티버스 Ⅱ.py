# 실행시간: 568 ms
# 메모리: 49092 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/18869
# Reference: 
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
dic = {}
for _ in range(m):
    planets = list(map(int, input().split()))
    s = sorted(list(set(planets)))
    ranked = {s[i]: i for i in range(len(s))}
    v = tuple([ranked[i] for i in planets])
    dic[v] = dic.get(v, 0) + 1
    print(dic)

answer = 0
for i in dic.values():
    answer += i*(i-1)//2
print(answer)