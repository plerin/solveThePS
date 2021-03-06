'''
>> P
한 행이 2**n인 정사각배열이 주어질 때 Z모양으로 탐색하려고 한다
N > 1 인 경우 2**(n-1)으로 4등분 후 재귀적으로 순서 방문
r행, c열을 몇 번째로 방문하는가?

>> S
같은 규칙을 갖는 것이 중첩됨 --> 분할 정복

N이 0일 될 때까지 1~4분면을 나눠 계산
'''

N, r, c = map(int, input().split())

ans = 0

# N > 1이면 계속 범위를 좁혀가며 크기만 쿠기 더해줘
while N != 0:

    N -= 1

    # 1사분면에 있는 경우 (사분면마다 시작하는 값이 다르기에 구분함)
    if r < 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 0

    # 2사분면 = c가 2**(N-1) 보다 큰 경우
    elif r < 2 ** N and c >= 2 ** N:
        ans += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N)   # r는 그대로 / c는 2**(N-1)만큼 줄어들어

    # 3사분면 = r이 2**(N-1) 보다 큰 경우
    elif r >= 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)   # c는 그대로 / r은 2**(N-1)만큼 줄여

    # 4사분면
    else:
        ans += (2 ** N) * (2 ** N) * 3
        r -= (2 ** N)
        c -= (2 ** N)

print(ans)
