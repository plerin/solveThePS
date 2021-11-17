'''
> P
M이상 N이하의 모든 소수를 출력하라 (띄어쓰기 구분)
> S
구현
에라토스테네스의 체 사용
    1. 구해야할 범위의 리스트 만들어놓기 _ 소수아님 체크용
    2. 2부터 범위의 max 값까지 반복하며 소수 리스트에 담고 그 수의 배수를 수수 아님 체크

함수(getPrime)
    - param : start(int) _ 시작값 == m
    - variable : check(list) _ max범위까지 리스트 _False로 초기
    - logic : start 부터 n까지 진행, 이중 반복문으로 i*i 부터 i씩 커지면서 check = True
'''

import sys

input = sys.stdin.readline


def findPrime(start, end):
    check = [False for _ in range(end+1)]
    prime = []

    for i in range(2, end+1):
        if check[i] == True:
            continue

        if i >= start:
            prime.append(i)

        for j in range(i*i, end+1, i):
            check[j] = True

    return prime


M, N = map(int, input().split())

ret = findPrime(M, N)

print(*ret, sep='\n')
