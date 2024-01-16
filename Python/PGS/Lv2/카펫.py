def solution(brown, yellow):
    answer = []
    by = brown + yellow
    for b in range(1, by+1):
        if (by / b) % 1 == 0: 
            a = by / b
            if a >= b:
                # (a-2)*(b-2) = yellow
                # 가로 2a + 세로 2b + 모서리 4 = brown 
                if 2*a + 2*b == brown + 4:
                    return[a, b]
        
    return answer