def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) - 1
    people.sort()
    check = False

    while(left < right):
        if people[right] + people[left] <= limit:
            left += 1
            answer += 1
        right -= 1
    
    return len(people) - answer
    

    # while(people):
    #     for i in range(len(people)-1, 0, -1):
    #         if people[0] + people[i] <= limit:
    #             answer += 1
    #             people.remove(people[i])
    #             people.remove(people[0])
    #             check = True
    #             break
    #     if(check):
    #         check = False
    #     else:
    #         answer += 1
    #         people.remove(people[0])
    # 정확도 테스틑 모두 통과하나, 효율성 통과 못함
    # remove() 사용하지 않고 다시 풀기
    # 다시 풀기..
