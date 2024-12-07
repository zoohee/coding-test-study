# 실행시간: 164ms
# 메모리: 31120KB
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/9017
# Reference: me
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cross = list(map(int, input().split()))
    max_num = max(cross)
    
    rank = [0 for _ in range(len(cross))]
    score = 1
    for i in range(len(cross)):
        if cross.count(cross[i]) < 6:
            continue
        else:
            rank[i] = score
            score += 1
    
    dict = {}
    cnt_dict = {}
    for i in range(len(rank)):
        if rank[i] != 0:
            if cross[i] in dict.keys():
                if cnt_dict[cross[i]] < 4:
                    dict[cross[i]] += rank[i]
                    cnt_dict[cross[i]] += 1
            else:
                dict[cross[i]] = rank[i]
                cnt_dict[cross[i]] = 1
    
    # 이제 여기서 동점인 팀의 다음 선수 점수를 비교해서 우승 정해주기
    min_score = min(dict.values())
    
    winner = 0
    winner_index = len(cross)
    for i in dict.keys():
        cnt = 0
        if dict[i] == min_score:
            for j in range(len(cross)):
                if cross[j] == i:
                    cnt += 1
                if cnt == 5:
                    if winner_index > j:
                        winner_index = j
                        winner = cross[j]
                    break
                
    print(winner)