'''
>> P
예제를 보고 규칙을 유츄한 뒤 별을 찍기
    - N은 항상 3*2**k수로 커진다. (3, 6, 12, 24, ..)
>> S

'''

# 풀이 1. N=3이 아닐 때 기본 모델을 양 옆으로 복사

# n = int(input())

# graph = [[' ', ' ', '*', ' ', ' '], [' ', '*',
#                                      ' ', '*', ' '], ['*', '*', '*', '*', '*']]


# def recursive(N, before):
#     # 행을 2배씩 늘어나, 열을 행보다 * 2 -1
#     after = [[' '] * (2 * 2 * N - 1) for _ in range(2 * N)]

#     # 2배씩 늘어날 때 윗줄
#     for i in range(N):
#         # N이 3이면 3:8 -> vvv + vv*vv
#         after[i][N:N+2*N-1] = before[i]

#     # 아랫 줄 , 삼각형 2개 그려야해서 k를 이용해 라인단위로 그림
#     k = 0
#     for i in range(N, 2 * N):
#         # 첫 번째 삼각형
#         after[i][:2*N] = before[k]
#         # 두 번째 삼각형
#         after[i][2*N: 2*N+len(before[k])] = before[k]
#         k += 1

#     # 커진 삼각형이 입력 값이면
#     if 2 * N == n:
#         return after

#     return recursive(2 * N, after)


# if n == 3:
#     result = graph
# else:
#     result = recursive(3, graph)

# for i in result:
#     print(''.join(i))


# 풀이 2. n=3일 때 그래프를 양옆으로 복사해나가는 개념
# -> 다음 모양부터 좌표만 계산해서 재귀적으로 그린다.

n = int(input())
# 최대 크기를 디폴트(' ')로 그린다.
graph = [[' '] * 2 * n for _ in range(n)]


def recursive(x, y, N):
    if N == 3:
        # 루트 좌표
        graph[x][y] = '*'
        # 2번째 줄
        graph[x+1][y-1] = graph[x+1][y+1] = '*'
        # 3번째 줄_ root(x,y)기준으로 x는 +2, y는 -2~+2까지니까 range(-2,3)
        for i in range(-2, 3):
            graph[x+2][y+i] = '*'
    else:
        next_N = N // 2
        recursive(x, y, next_N)
        recursive(x+next_N, y-next_N, next_N)
        recursive(x+next_N, y+next_N, next_N)


recursive(0, n-1, n)
for i in graph:
    print(''.join(i))
