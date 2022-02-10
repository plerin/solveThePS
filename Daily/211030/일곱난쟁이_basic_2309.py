'''
[P]
9명의 난쟁이 중 진짜 일곱 난쟁이를 찾아라
    - 7명 키의 합이 100이고 여러 경우 중 하나 출력
[S]
9명 중 7명을 임의로 골라 키의 합이 100인지 맞춰보기 _ 브루트 포스 OR 조합(from intertools import combinations) 
[L]
조합으로 임의로 7명 뽑는 경우의 수 중 키의 합이 100인 경우 리턴
'''

from itertools import combinations

dwarps = [int(input()) for _ in range(9)]

for comb in combinations(dwarps, 7):
    if sum(comb) == 100:
        print(*sorted(comb), sep='\n')
        exit()
