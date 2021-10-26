'''
[P]
N이 주어졌을 때, N번째 피보나치 수를 구하는 프로그램 작성
    - 식 : Fn = Fn-1 + Fn-2 (n>=2)
[S]
구현(implementation) _ 식이 주어지고 코드로 구현
    - 재귀 _ recursive하게 풀이
[L]
1. 함수 이용
    - PARAM : n(int) _ 입력 값이며 n번째 피보나치 수를 구하기 위함
    - LOGIC :
        1) 기저조건 설정 : if n <= 1 then return n
        2) else then return factorial(n-1) + factorial(n-2)
'''


def factorial(n):
    if n <= 1:
        return n
    else:
        return factorial(n-1) + factorial(n-2)


n = int(input())

ret = factorial(n)

print(ret)
