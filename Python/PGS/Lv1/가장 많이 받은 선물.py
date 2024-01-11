import itertools

def solution(friends, gifts):
    answer = 0

    # 각 이름에 인덱스 지정
    index = {}
    for i in range(len(friends)):
        index[friends[i]] = i
    
    # 선물 기록하기
    score = [[0]*len(friends) for _ in range(len(friends))]
    
    for gift in gifts:
        aa, bb = map(str, gift.split(" "))
        a = index[aa]
        b = index[bb]
        score[a][b] += 1
    print(score)
    
    # 각 사람마다 준 선물과 받은 선물 수 세기
    gift_score = [[0] * 3 for _ in range(len(friends))]
    print(gift_score)
    for i in range(len(friends)):
        for j in range(len(friends)):
            gift_score[i][0] += score[i][j] # 준 선물
            gift_score[j][1] += score[i][j] # 받은 선물
    
    # 선물 지수 계산
    for i in range(len(friends)):
        gift_score[i][2] = gift_score[i][0] - gift_score[i][1]
    
    print(gift_score)
            
    # 다음 달에 받을 선물 계산    
    next_month = [0 for _ in range(len(friends))]
    for aa, bb in itertools.combinations(friends, 2):
        a = index[aa]
        b = index[bb]
        # 자기 자신은 넘어감
        if a==b:
            continue
        # 기록이 없거나 선물 주고 받은 수가 같을 때
        if (score[a][b] == score[b][a]): 
            # 선물 지수가 더 높은 a가 다음 달에 선물 받음
            if gift_score[a][2] > gift_score[b][2]:
                next_month[a] += 1
            elif gift_score[a][2] < gift_score[b][2]:
                next_month[b] += 1
        # 기록이 있을 때
        else:
            # 준 선물이 더 많은 사람이 다음 달에 선물 받음
            if score[a][b] < score[b][a]:
                next_month[b] += 1
            else:
                next_month[a] += 1

    answer = max(next_month)
    return answer