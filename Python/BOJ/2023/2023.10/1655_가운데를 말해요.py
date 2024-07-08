import sys
input = sys.stdin.readline
import heapq

n = int(input())
min_heap = [] # 중간값보다 큰 값
max_heap = [] # 중간값보다 작거나 같은 값
median = int(input())
print(median)
for _ in range(1, n):
    value = int(input())

    if value > median: # 중간값보다 크면
        heapq.heappush(min_heap, value) # 최소힙에 저장
        if len(min_heap) - len(max_heap) > 1: # 최소힙이 항상 1개 많음까지만 유지
            heapq.heappush(max_heap, -median)
            median = heapq.heappop(min_heap)
    else: # 중간값보다 작거나 같으면
        heapq.heappush(max_heap, -value)
        if len(min_heap) < len(max_heap): # 최대힙이 큼 유지
            heapq.heappush(min_heap, median)
            median = -heapq.heappop(max_heap)
            
    # print("===========")
    # print(max_heap)
    # print(min_heap)
    print(median)