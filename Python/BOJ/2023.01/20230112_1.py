#1919 에너그램 만들기
import sys
input = sys.stdin.readline

a = list(input())
b = list(input())

a1, b1 = a[:], b[:]
out1 = [x for x in a if not x in b1 or b1.remove(x)]
out2 = [x for x in b if not x in a1 or a1.remove(x)]

print(len(out1)+len(out2))

# a = input()
# b = input()
# len_b = len(b)
# same_cnt = 0
# for i in a:
#     if i in b:
#         b= b.replace(i, '', 1)
#         same_cnt += 1
# print(len(a) + len_b - 2 * same_cnt)