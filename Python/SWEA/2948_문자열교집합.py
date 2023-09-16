# 시간복잡도: O(n)
# 최악시간: 
# 난이도: D3
# Url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-Un3G64SUDFAXr&
# Reference: Me
# 메모리 : 201996kb
# 실행시간 : 1804ms

answer = set()

test_case = int(input())
for t in range(test_case):
    n, m = map(int, input().split())
    a = list(input().split())
    b = list(input().split())
    ab = a + b
    print("#",t+1," ",len(ab)-len(set(ab)), sep="")
        
