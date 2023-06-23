# 시간복잡도: 
# 최악시간: 
# 난이도: Lv2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/49994
# Reference: https://velog.io/@ehddms7410/Algo-%EA%B5%AC%ED%98%84-50%EB%AC%B8%EC%A0%9C#12-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4---%EB%B0%A9%EB%AC%B8-%EA%B8%B8%EC%9D%B4
def solution(dirs):
    move = {'U':[0,1],'D':[0,-1],'R':[1,0],'L':[-1,0]}
    answer = []
    x,y = 0,0
    for dir in dirs:
        xx,yy = x + move[dir][0], y + move[dir][1]
        if xx < -5 or xx > 5 or yy < -5 or yy > 5:
            continue
        if [str(x)+str(y), str(xx)+str(yy)] not in answer:
            answer.append([str(x)+str(y), str(xx)+str(yy)])
            answer.append([str(xx)+str(yy), str(x)+str(y)])
        x, y = xx, yy
    return len(answer) // 2