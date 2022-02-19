'''
backjoon url -> https://www.acmicpc.net/problem/1629
youtube url -> https://www.youtube.com/watch?v=HQvL9My2Y6o
concept url -> https://hongjw1938.tistory.com/193

분할 정복(Divide and Conquer)

>> Concept

큰 문제를 작은 문제로 분할하여 풀고 그 결과를 사용하여 큰 문제를 푸는 방법
일반적인 탐색으로 풀이하면 시간 초과나는 경우 의심해보기

시간복잡도
- O(logN)

>> P 
A를 B번 곱한 수를 알고 싶다 C로 나눈 나머지를 출력하라
    - 범위 -> A,B,C 모두 ~ 21억

>> S
값이 너무 크기 때문에 연산 분배법칙 활용 
(A + B) % p = ((A % p) + (B % p)) % p
(A * B) % p = ((A % p) * (B % p)) % p
(A - B) % p = ((A % p) - (B % p) + p) % p

접근
1. 입력 받은 값으로 재귀함수 호출
2. 재귀함수 선언
def solve(a, b) -> int:
    if b == 1:
        return a % c
    
    ret = solve(a, b//2)
    
    if b % 2 == 1:
        ret = ret* ret * a
    else:
        ret *= ret
    
    return ret 
3. 결과 출력 
'''


def solve(a, b) -> int:
    if b == 1:
        return a % c

    ret = solve(a, b//2)

    if b % 2 == 1:
        ret = ret**2 * a
    else:
        ret = ret**2

    return ret % c


a, b, c = map(int, input().split())

print(solve(a, b))
