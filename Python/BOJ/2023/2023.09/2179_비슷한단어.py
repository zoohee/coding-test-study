# 시간복잡도: 
# 최악시간: 
# 난이도: Silver 3
# Url: https://www.acmicpc.net/problem/2179
# Reference: 

import sys
input = sys.stdin.readline

n = int(input())
input_words = [input().rstrip() for _ in range(n)]
dict_index = dict.fromkeys(input_words, 0)
for i in range(n):
    dict_index[input_words[i]] = i
words = sorted(input_words)
print(words)

maxCnt = 0
minIndex = n
a = ""
b = ""
for i in range(n-1):
    j = i+1
    if (words[i] == words[j]): # 같으면 건너 뛰기
        continue
    length = min(len(words[i]), len(words[j]))
    cnt = 0
    for k in range(length):
        if(words[i][k] == words[j][k]):
            cnt += 1
        else:
            break
    
    if (maxCnt < cnt):
        maxCnt = cnt
        if(dict_index[words[i]]<dict_index[words[j]]):
            a = words[i]
            b = words[j]
            minIndex = dict_index[words[i]]
        else:
            a = words[j]
            b = words[i]
            minIndex = dict_index[words[j]]
    elif (maxCnt == cnt):
        if(minIndex > dict_index[words[i]] and
           minIndex > dict_index[words[j]]):
            if(dict_index[words[i]] < dict_index[words[j]]):
                a = words[i]
                b = words[j]
                minIndex = dict_index[words[i]]
            else:
                a = words[j]
                b = words[i]
                minIndex = dict_index[words[j]]   
        elif(minIndex > dict_index[words[i]]):
            a = words[i]
            b = input_words[minIndex]
            minIndex = dict_index[words[i]]
        elif(minIndex > dict_index[words[j]]):
            a = words[j]
            b = input_words[minIndex]
            minIndex = dict_index[words[j]]
        else:
            if(minIndex == dict_index[words[i]]):
                a = input_words[minIndex]
                b = input_words[min(dict_index[b], dict_index[words[j]])]
            elif(minIndex == dict_index[words[j]]):
                a = input_words[minIndex]
                b = input_words[min(dict_index[b], dict_index[words[i]])]
            else:
                a = input_words[minIndex]
                b = input_words[min(dict_index[b], dict_index[words[i]], dict_index[words[j]])]
                
print(a+"\n"+b)
# 이거 무조건 카운트 같으면 리스트에 같은거 다 추가하면서 해야됨.
# 안그러면 쌩뚱맞게 카운트 안된 단어 들어갈 수도 있음
# 4
# aa
# bb
# bc
# aj
# -- 현재출력
# aa
# bb
# -- 정답
# aa
# aj


# 5
# a
# ab
# abv
# abaa
# abdd

# 9
# ab
# is
# lunch
# for
# most
# waits
# until
# two
# ac

# 4
# aa
# bb
# bc
# aj