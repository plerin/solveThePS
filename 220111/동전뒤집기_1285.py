'''
>> P
N*N 행렬에서 행 / 열을 모두 뒤집는 연산을 통해 뒷면('T')이 위를 향하는 동전 개수가 최소가 될 때 개수를 구하라
    - 동전 : 앞면 = 'H' / 뒷면 = 'T'
    - 연산 : 한 행 / 한 열을 모두 뒤집는다(H <-> T)
>> S
모든 경우를 구하여 뒷면이 최소가 되는 경우 찾기
    -> 완전탐색 / 그리디

전략
1. 모든 행마다 뒤집는 경우를 계산
    -> 한 행의 경우 == 뒤집는다 / 안 뒤집는다 == 2가지 
    -> 3행 == 2**3 == 8
2. 모든 경우에서 열로 탐색하며 뒷면개수를 찾고 행렬의 합을 갖고 최솟값 갱신
    -> ans = n*n+1
    -> tot += min(cnt, N-cnt) # T개수가 H보다 적으면 toggle(뒤집고) T 개수를 카운트(==N-cnt)
'''
import sys

input = sys.stdin.readline


def solve():
    ret = (N * N) + 1   # 최대 값 저장

    for i in range(1 << N):  # 모든 경우의 수를 비스마스크로 반복(3행이면 2**3)
        tmp = [coin[c][:] for c in range(N)]    # 입력 값 불러오기
        tot = 0

        for x in range(N):
            if i & (1 << x):    # 현재 경우의 수에 해당하는 행만 toggle
                for y in range(N):
                    if tmp[x][y] == 'H':
                        tmp[x][y] = 'T'
                    else:
                        tmp[x][y] = 'H'

        tot = 0
        for x in range(N):
            cnt = 0
            for y in range(N):
                if tmp[y][x] == 'T':
                    cnt += 1
            tot += min(cnt, N-cnt)  # T보다 H가 많은 경우 열을 toggle 후 뒷면 카운트 == N-cnt

        ret = min(ret, tot)
    return ret


N = int(input())
coin = [list(input().rstrip()) for _ in range(N)]

ans = solve()

print(ans)
