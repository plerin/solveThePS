'''
> P
4보다 큰 짝수는 두 홀수의 합으로 나타낼 수 있을 때 조합 반환
> S
유형 : 수학
접근
    1. 입력 받은 짝수를 MAX로 한 소수 리스트를 구함
    2. START(0)/END(LEN()-1)로해서 WHILE START <= END THEN [END]-[START] = VAL 인 경우 찾아 크면 END 왼쪽, 작으면 START 오른족
    3. 출력

함수(verifyGuess)
    - purpose : 문제의 가설이 맞는지 _ 특정 값에 대한 소수 구하고 홀수의 합 구하기
    - param : num(int) : 입력 값
    - logic
        1. num을 최대 값으로 하는 소수 리스트 구하기
        2. 소수 리스트를 start/end로 반복문 돌려 합인 경우 구하기
        3. 결과 반환 / 없으면 0
    - return : ans(list)_없으면 빈 리스트
'''

import sys

input = sys.stdin.readline

MAX = 1000001

check = [True] * MAX

for i in range(2, int(MAX**0.5)+1):
    if check[i] == True:
        for j in range(i*i, MAX, i):
            check[j] = False

while True:
    n = int(input())

    if n == 0:
        break

    ret = []

    for i in range(3, n+1):  # 홀수 & 소수 이여야하니까 3부터 시작
        if check[i] == True and check[n-i] == True:
            ret = [i, n-i]
            break

    if len(ret) == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f'{n} = {ret[0]} + {ret[1]}')
