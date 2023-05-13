def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += price * (i+1)
    if answer < money:
        return 0
    else:
        answer = answer - money
        return answer

print(solution(3, 30, 4))


# def solution(price, money, count):
#     return max(0,price*(count+1)*count//2-money)