#10804
import sys
input = sys.stdin.readline

cards = [i+1 for i in range(20)]

for i in range(10):
    m, n = map(int,input().split())
    a = cards[:m-1] # m--1번째까지 베열 저장
    b = cards[m-1:n][::-1] # m--1~n번째까지 배열 역순 저장
    c = cards[n:] #n~끝까지 배열 저장
    cards = a + b + c
    
for i in cards:
    print(i, end=' ')