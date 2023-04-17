# 시간복잡도:
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
from itertools import permutations

N,M = map(int, input().split(' '))
print('\n'.join(list(map(' '.join, permutations(map(str, range(1, N+1)), M)))))

# permutation은 순열
# nPr

# n,m = list(map(int,input().split()))
 
# s = []
 
# def dfs():
#     if len(s)==m:
#         print(' '.join(map(str,s)))
#         return
    
#     for i in range(1,n+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()
 
# dfs()
# https://jiwon-coding.tistory.com/21