'''
youtube url -> https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2&t=758s

>> Keyword
그리디 알고리즘, 아이디어를 발견하고 정당성으로 검증

>> P
N이 1일 될 때까지 두 과정 중 하나를 반복적으로 수행
N과 K가 주어질 때 N이 1이 될 때까지 과정을 수행하는 최소 횟수를 구하라
1. N에서 1을 빼기
2. N을 K로 나누기(K로 나누어 떨어지는 경우에만 사용가능)

>> S
2가지 방법 중 더 효과적인 방법은 2번(K로 나누기)
-> K로 나누어 떨어지는지 확인하고 떨어지면 2번 수행 아니면 1번 수행하며 카운트 진행
-> 그리디 알고리즘(효율적인것을 우선 수행)

정당성판단
K는 2부터 시작하므로 어떤 값이든 1을 빼는 거보다 효과적임

코드
1. 메소드 선언
def solve(num: int, div: int) -> int:
    ret = 0
    
    while num != 1:
        if num % div:
            num %= div
        else:
            num -= 1
        ret += 1
    
    return ret

'''

# 일반적인 풀이 _ 1,2번 연산을 수행 뒤 반복함


def solve2(num: int, div: int) -> int:
    ret = 0

    while num != 1:
        s, r = divmod(num, div)
        if r == 0:
            num = s
        else:
            num -= 1

        ret += 1

    return ret

# 효율적인 풀이 O(logN) _ 1번 연산 수행횟수를 없앰 -> 빠름


def solve(num: int, div: int) -> int:

    ret = 0

    while True:
        # num이 div로 나누어 떨어질 때까지 1번 연산 수행(한번에)
        target = (num // div) * div
        ret += (num - target)
        num = target
        # 더 이상 나누어 지지 않을 때
        if num < div:
            break
        # div으로 나누기
        ret += 1
        num //= div

    ret += (num-1)
    return ret


N, K = map(int, input().split())
print(solve(N, K))
