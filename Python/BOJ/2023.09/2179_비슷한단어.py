# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/2179
# Reference: 

import sys
input = sys.stdin.readline

n = int(input())
word = list(input().rstrip())
words = [input().rstrip() for _ in range(n-1)]
