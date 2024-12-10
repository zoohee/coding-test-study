def solution(today, terms, privacies):
    answer = []
    dict = {}
    for t in terms:
        key, value = t.split()
        dict[key] = int(value)*28
        
    ty, tm, td = today.split('.')
    today_day = int(ty)*336 + int(tm)*28 + int(td)
    
    # 파기해야 할 개인 정보
    idx = 1
    for priv in privacies:
        date, rule = priv.split()
        y, m, d = date.split('.')
        iy, im, id = int(y), int(m), int(d)
        day = iy*336 + im*28 + id + dict[rule]
        if day <= today_day:
            answer.append(idx)
        idx += 1
        
    return answer