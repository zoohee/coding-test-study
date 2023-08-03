def solution(n, lost, reserve):
    # 0: 도난당함 1: 여벌 없음 2: 여벌 있음
    answer = 0
    have = [1] * (n+1)
    reserve = set(reserve)
    lost = set(lost)
    for i in range(len(reserve)):
        have[reserve[i]] = 2
        
    for i in range(len(lost)):
        have[lost[i]] = 0
        
    for i in range(1, n+1):
        if have[i] == 0:
            if not i == 1:
                if have[i-1] == 2:
                    have[i-1] = 1
                    have[i] = 1
                    
        if have[i] == 0:
            if not i == n:
                if have[i+1] == 2:
                    have[i+1] = 1
                    have[i] = 1
                
    for i in range(1, n+1):
        if have[i] == 1 or have[i] == 2:
            answer += 1
    return answer

print(solution(3, [3], [1]))

# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)