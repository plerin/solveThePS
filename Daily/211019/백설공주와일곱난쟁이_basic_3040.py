'''
kp
#1. 조합(combination)으로 경우를 찾고 합이 100인 경우 출력
'''
from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]

comb = combinations(dwarfs, 7)

for lst in comb:
    if sum(lst) == 100:
        print(*lst, sep='\n')
