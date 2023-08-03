# 시간복잡도: 
# 최악시간: 
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
num = [i for i in range(n)]
team_list = list(combinations(num, n//2))

min_stats = 999999

for i in range(len(team_list)//2):
    start = 0
    link = 0
    team = team_list[i]
    another_team = [x for x in num if x not in team_list[i]]
    
    for j in team:
        for k in team:
            start += stats[j][k]

    for j in another_team:
        for k in another_team:
            link += stats[j][k]

    min_stats = min(min_stats, abs(start-link))

print(min_stats)