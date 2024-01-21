def solution(storey):
    answer = 0
    # 절댓값이 1이거나 10으로 나누어 떨어지는 버튼이 있음
    while(True):
        if storey <= 0:
            break
        
        if storey % 10 > 5:
            answer += 10 - storey % 10
            storey += storey % 10
        # 자리수가 바뀌는 경우 고려해야 함  
        elif storey % 10 == 5:
            answer += 5
            # 현재 5일 때 다음 자리수가 4 이하면 반올림하면 안된다
            if storey >= 10:
                tmp = storey // 10
                if tmp % 10 >= 5:
                    storey += 10
        else:
            answer += storey % 10
            storey -= storey % 10
        
        storey = storey // 10
            
    return answer