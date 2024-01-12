def solution(data, ext, val_ext, sort_by):
    answer = []
    index = 0
    for d in data:
        if ext == "code": index = 0
        elif ext == "date": index = 1
        elif ext == "maximum": index = 2
        else: index = 3
        if d[index] < val_ext:
            answer.append(d)
            
    if sort_by == "code":
        answer.sort(key = lambda x:x[0])
    elif sort_by == "date":
        answer.sort(key = lambda x:x[1])
    elif sort_by == "maximum":
        answer.sort(key = lambda x:x[2])
    else:
        answer.sort(key = lambda x:x[3])
    
    return answer