
# 풀이 1. 공간을 9개로 나눈 뒤 1번 공간의 별을 5번 공간 제외한 나머지에 복사

import sys

sys.setrecursionlimit(10**6)


def paint_star(len):
    div3 = len // 3

    # base_condition
    if len == 3:
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*'] * 3
        return

    paint_star(div3)    # 9개 구역으로 나눈 뒤 재귀 호출 _ 가장 작은 구역(len==3) 나올 때까지

    # range(0, len, div3)으로 탐색하면 구역의 시작 지점만 탐색한다
    for i in range(0, len, div3):
        for j in range(0, len, div3):
            # i == div3 and j == div3 이면 5번째 공간(빈칸)을 의미
            if i != div3 or j != div3:
                # base_condition에서 만든 1번째 공간(별)을 다른 공간으로 복사하는 작업
                for k in range(div3):
                    g[i+k][j:j+div3] = g[k][:div3]


def paint_star2(len):
    div3 = len // 3

    if len == 3:
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*'] * 3
        return

    paint_star2(div3)

    # 별 크기가 켜져도 똑같이 복사(5번 제외한 공간에 1번 별을 복사)
    for i in range(0, len, div3):
        for j in range(0, len, div3):
            if i != div3 or j != div3:
                for k in range(div3):
                    # 1번 공간의 별을 5번을 제외한 모든 공간(2~9)에 복사
                    g[i+k][j:j+div3] = g[k][:div3]


n = int(input())
# 모든 크기를 디폴트(' ')로 잡아둬
g = [[' ' for _ in range(n)] for _ in range(n)]

paint_star2(n)

for row in g:
    print(*row, sep='')


# 풀이 2. 공간을 1,2,3행으로 나눈 후 재귀함수를 통해 구해진 별을 붙인다.

# sys.setrecursionlimit(10**6)


# def append_star(len: int) -> list:

#     if len == 1:    # base_condition
#         return ['*']

#     stars = append_star(len//3)
#     l = []

#     # 행을 1,2,3으로 나눠 작은 사각형부터 큰 사각형으로 붙여준다.
#     for s in stars:
#         l.append(s*3)
#     for s in stars:
#         l.append(s + ' '*(len//3) + s)
#     for s in stars:
#         l.append(s*3)

#     return l


# n = int(input())
# print('\n'.join(append_star(n)))
