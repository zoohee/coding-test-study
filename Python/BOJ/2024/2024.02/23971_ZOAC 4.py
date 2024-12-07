# 실행시간: 40ms
# 메모리: 33240KB
# 난이도: Bronze 3
# Url: https://www.acmicpc.net/problem/23971
# Reference: https://janghan-kor.tistory.com/953

import sys
import math
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

A = math.ceil(H/(N+1))
B = math.ceil(W/(M+1))

print(A*B)         