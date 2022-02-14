'''
모든 재귀 함수는 반복문을 이용하여 동일한 기능 구현할 수 있음

장점 : 점화식을 그대로 사용하여 간결
단점 : 메모리를 많이 사용하는 단점

1. 팩토리얼 예제
점화식 : n! = n * (n-1)!
'''


def factorial_iterative(n):
    ret = 1

    for i in range(1, n+1):
        ret *= i

    return ret


def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n-1)


print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))
