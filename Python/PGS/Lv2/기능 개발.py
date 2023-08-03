def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] == 0:
            days.append((100-progresses[i])//speeds[i])
        else:
            days.append(((100-progresses[i])//speeds[i])+1)
    
    count = 0
    max_day = days[0]
    for i in range(1, len(days)):
        count += 1
        if max_day < days[i]:
            answer.append(count)
            count = 0
            max_day = days[i]
        if i == len(days)-1:
            if max_day < days[i]:
                answer.append(count)
            else:
                answer.append(count+1)
    return answer