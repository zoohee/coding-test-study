import sys
input = sys.stdin.readline

def binary_search():
    start = 0 
    end = max(line)

    while start <= end:
        mid = (start + end) // 2 
        cnt = 0
        for l in line:
            cnt += l // mid
        
        # 랜선의 길이 움직이기
        if cnt >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]

print(binary_search())