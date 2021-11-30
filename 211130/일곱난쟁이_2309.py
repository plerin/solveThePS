'''
9중 7 난쟁이 키 조합을 구하고 그 합이 100인경우 출력

from itertools import combinations 
'''

from itertools import combinations

dwarf = [int(input()) for _ in range(9)]

for comb in combinations(dwarf, 7):
    if sum(comb) == 100:
        print(*sorted(comb), sep="\n")
        break
