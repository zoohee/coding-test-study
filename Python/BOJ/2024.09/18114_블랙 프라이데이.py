# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
from itertools import combinations
from bisect import bisect_left

# 입력 받기
N, C = map(int, input().split())
weights = list(map(int, input().split()))

# Meet in the middle: 배열을 두 부분으로 나눔
half = N // 2
left_weights = weights[:half]
right_weights = weights[half:]

# 각 부분의 부분 집합의 합을 구하는 함수
def get_subset_sums(arr):
    subset_sums = []
    n = len(arr)
    for i in range(n+1):
        for comb in combinations(arr, i):
            subset_sums.append(sum(comb))
    return subset_sums


left_sums = get_subset_sums(left_weights)
right_sums = get_subset_sums(right_weights)


right_sums.sort()

# 가능한 합을 찾기
found = False
for s in left_sums:
    target = C - s
    # 이분 탐색으로 right_sums에서 target 이상인 값을 찾음
    idx = bisect_left(right_sums, target)
    if idx < len(right_sums) and right_sums[idx] == target:
        found = True
        break

# 결과 출력
if found:
    print(1)
else:
    print(0)
