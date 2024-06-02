# 실행시간: 152 ms
# 메모리: 43900 KB
# 난이도: Gold 4
# Url: https://www.acmicpc.net/problem/13144
# Reference: https://99uulog.tistory.com/85
import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

s, e = 0, 0
dup = set() # 검색 O(n)
res = 0
while (s != n) and (e != n):
    if nums[e] not in dup:
        dup.add(nums[e])
        e += 1
        res += e - s
    else:
        while nums[e] in dup:
            dup.remove(nums[s])
            s += 1

print(res)