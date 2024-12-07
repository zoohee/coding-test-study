# 실행시간: 288 ms
# 메모리: 31120 KB
# 난이도: Gold 5
# Url: https://www.acmicpc.net/problem/20437
# Reference: https://blog.naver.com/jinhan814/222436910915
from collections import defaultdict
import sys
input = sys.stdin.readline

def length(cnt):
    min_l = len(w)
    max_l = -1
    
    for i in cnt:
        # 문자 정확히 2개만 포함 (양끝)
        for j in range(len(i) - k + 1):
            length = i[j+k-1] - i[j] + 1
            min_l = min(min_l,length)
            max_l = max(max_l,length)
    
    return(min_l,max_l)
    

t = int(input())
for _ in range(t):
    w = list(map(lambda x: ord(x) - 97, input().strip()))
    k = int(input())
    
    cnt = [[] for _ in range(26)]
    for idx, val in enumerate(w):
        cnt[val].append(idx) # 알파벳 등장 인덱스 저장
    
    mn, mx = length(cnt)
    print(-1 if mx == -1 else f"{mn} {mx}")
        