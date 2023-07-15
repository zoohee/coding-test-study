# 시간복잡도: 
# 최악시간: 
# 난이도: Lv 2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/49993
# Reference: Me
def solution(skill, skill_trees):
    answer = 0
    
    for i in range(len(skill_trees)):
        skill_check = [False] * len(skill)
        breakpoint = False
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                for k in range(len(skill)):
                    if skill[k] == skill_trees[i][j]:
                        if k == 0:
                            skill_check[0] = True
                        else:
                            skill_check[k] = True
                            for l in range(k):
                                if skill_check[l] == False:
                                    breakpoint = True
                                    break
                    if breakpoint:
                        break
            if breakpoint:
                break
        if breakpoint == False:
            answer += 1
    return answer

# 다른 사람 풀이
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer