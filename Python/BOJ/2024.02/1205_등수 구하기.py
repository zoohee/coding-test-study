# 실행시간: ms
# 메모리: KB
# 난이도: 
# Url: https://www.acmicpc.net/problem/
# Reference: 
import sys
input = sys.stdin.readline

n, new, p = map(int, input().split())
if n>0:
    score = list(map(int, input().split()))
else:
    print(1)
    exit(0)
    

# p는 랭킹리스트의 길이
# new 가 몇등인지 구해라
# 점수가 못들어가면 -1

isInsert = False
for i in range(len(score)-1, -1, -1):
    if score[i] >= new and len(score) <= p:
        if i == len(score)-1:
            print(-1)
            exit(0)
        tmp = score[i+1:len(score)]
        score = score[:i+1]
        score.append(new)
        isInsert = True
        if len(score) > p:
            score = score + tmp[:len(tmp)-1]
        else:
            score = score + tmp[:len(tmp)]
        break
    else:
        continue

if not isInsert:
    print(1)
    exit(0)

cnt = 1
a = score[0]
for i in range(1, len(score)):
    if score[i-1] != score[i]:
        cnt += 1
    if score[i] == new:
        print(i+1)
        break
