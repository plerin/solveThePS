'''
> P
양의 정수 n개가 주어졌을 때 가능한 모든 쌍의 GCD의 합
> S
수학
> L 
1. combinations를 활용해 모든 쌍을 구한다
2. 쌍에 대한 GCD 찾는 함수 
3. 결과 합 
'''

from itertools import combinations


def getGCD(a, b):
    return b if a % b == 0 else getGCD(b, a % b)


t = int(input())

for _ in range(t):
    n, *arr = list(map(int, input().split()))
    ret = 0

    for a, b in combinations(arr, 2):
        ret += getGCD(a, b)
    print(ret)
