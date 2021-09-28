from itertools import permutations
from itertools import combinations
# nCn을 의 합을 구하는 문제
N = int(input())
print(list(combinations(range(N+1), N)))
