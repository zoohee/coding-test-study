s = input()

def solution(s):
    return ''.join(sorted(s, reverse=True))

print(solution(s))