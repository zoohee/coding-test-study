# # 실행시간: 3060 ms
# # 메모리: 31120 KB
# # 난이도: Gold 5
# # Url: https://www.acmicpc.net/problem/22251
# # Reference: https://magentino.tistory.com/257
import sys
input = sys.stdin.readline
n, k, p, x = map(int, input().split())

num = {
  '0' : int('1111110', 2),
  '1' : int('0110000', 2),
  '2' : int('1101101', 2),
  '3' : int('1111001', 2),
  '4' : int('0110011', 2),
  '5' : int('1011011', 2),
  '6' : int('1011111', 2),
  '7' : int('1110000', 2),
  '8' : int('1111111', 2),
  '9' : int('1111011', 2)
}

x_num = str(x).rjust(k, '0')
answer = 0
for n in range(1, n+1):
    f_num = str(n).rjust(k, '0')
    cnt = 0
    for i in range(k):
        cnt += bin(num[x_num[i]] ^ num[f_num[i]]).count('1') # xor 연산 (다를 때)
    
    if 0 < cnt <= p:
        answer += 1

print(answer)
    