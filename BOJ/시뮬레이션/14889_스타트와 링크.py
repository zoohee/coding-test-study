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

print(stats)
print(team_list)

min_stats = 99

for i in range(len(team_list)//2):
    start = 0
    link = 0
    team = team_list[i]
    another_team = [x for x in num if x not in team_list[i]]
    
    # print(team)
    # print(another_team)
    
    for j in team:
        for k in team:
            start += stats[j][k]
    print(start)
    
    for j in another_team:
        for k in another_team:

                # print(stats[j][k])
                # print(stats[k][j])
            link += stats[j][k]

    # start = stats[team[i][0]][team[i][1]] + stats[team[i][1]][team[i][0]]
    # link = stats[another_team[0]][another_team[1]] + stats[another_team[1]][another_team[0]]
    # print("start")
    # print(start)
    # print("link")
    # print(link)
    # print(abs(start-link))
    min_stats = min(min_stats, abs(start-link))

print(min_stats)