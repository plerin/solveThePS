'''
문제의 핵심
1. 1~n까지 반복하며 x,y를 찾고 없는 경우 -1 리턴
    -> n(최대 값)을 어떻게 정할 것인가 -> 
    -> n*m의 최소 공배수 
    -> n*m
2. 테스트 케이스마다 입력 최대 값(4만)을 반복하면 시간제한 걸림 어떻게 해결가능
    -> x, y 둘다 확인할 필요 없이 x, y 둘 중 하나만 값을 변경하며 확인
    -> x = x + m ,, if x % N == y % N then return x else x += M

func(calDate)
    - param : n,m,x,y
    - vari : ret(int) _ 1부터 n까지 반복하며 x,y 나오면 리턴 
    - logic
        1) for i in range(n*m):
        2) if x % N == y % N then return x else x += M
'''


def calDate(m: int, n: int, x: int, y: int):

    while x <= (m*n):
        if x % N == y % N:
            return x
        else:
            x += M

    return -1


for i in range(int(input())):
    M, N, x, y = map(int, input().split())
    ans = calDate(M, N, x, y)

    print(ans)
