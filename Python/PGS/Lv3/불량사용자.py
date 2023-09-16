from itertools import product

def solution(user_id, banned_id):
    answer_list = []
    id_list = [[] for _ in range(len(banned_id))]
    
    # print(id_list)
    check = 1;
    index = 0;
    for b in banned_id:
        for u in user_id:
            if len(b)==len(u):
                for i in range(len(b)):
                    if b[i] == '*':
                        continue
                    if b[i] != u[i]:
                        check = 0
                        break
                if check:
                    id_list[index].append(u)
                else:
                    check = 1
        index += 1
    
    for i in product(*id_list): # 데카르트곱
        if len(banned_id)==len(set(i)):
            for ans in answer_list: # 누적된 정답 중에
                if len(ans - set(i)) == 0: # 순서만 다르고 원소는 똑같은 정답 있으면 얘는 제외
                    check = 0
                    break
            if check:
                answer_list.append(set(i))
            else:
                check = 1
    
    answer = len(answer_list)
    return answer