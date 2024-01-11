def solution(bandage, health, attacks):
    answer = 0
    # 1초마다 x 만큼의 체력 회복
    # t초마다 연속으로 붕대 감으면 y 만큼의 체력 추가 회복
    original_health = health
    attacks_index = 0
    bandage_time = 0
    # bandage는 [시전 시간, 초당 회복량, 추가 회복량]
    # 몬스터의 마지막 공격까지
    for i in range(1, attacks[len(attacks)-1][0]+1):
        if i == attacks[attacks_index][0]:
            bandage_time = 0
            health -= attacks[attacks_index][1]
            attacks_index += 1
        else:
            bandage_time += 1
            if health < original_health:
                health += bandage[1]
                if bandage_time == bandage[0]:
                    health += bandage[2]
                    bandage_time = 0
            else:
                bandage_time += 1
                
        if health > original_health:
            health = original_health
        if health <= 0:
                return -1

    answer = health
    return answer