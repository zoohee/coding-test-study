# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    # 각각 이 집을 선택했을 때의 최솟값이 저장됨.
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]
    
print(min(rgb[n-1]))

# 3
# 26 40 83
# 49 60 57
# 13 89 99
# 가 있을 때
# 앞뒤로 색이 같으면 안 됨
# i=1
# 1. 49(빨간색)가 선택된다면 40, 83 중 min > 49+40=89
# 2. 60(초록색)이 선택된다면 26, 83 중 min > 60+26=86
# 3. 57(파란색)이 선택된다면 26, 40 중 min > 57+26=83

# i=2
# 1. 13이 선택된다면 86, 83 중 min > 13+83=96
# 2. 89가 선택된다면 89, 83 중 min > 89+83=172
# 3. 99가 선택된다면 89, 86 중 min > 99+86=185


