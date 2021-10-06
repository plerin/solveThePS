'''
GOAL: 동적계획법을 활용해 외판원 순회 문제 풀기
1. 입력 받기
    1) 경로
'''


def tsp(dists):

    N = len(dists)
    VISITED_ALL = (1 << N)-1
    cache = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')

    def find_path(last, visited):
            if visited == VISITED_ALL:
                return dists[last][0] or INF

            if cache[last][visited] is not None:
                return cache[last][visited]

            tmp = INF
            for city in range(N):
                if visited & (1 << city) == 0 and dists[last][city] != 0:
                    tmp = min(tmp, find_path(city, visited |
                                            1 << city)+dists[last][city])
            # 여기선 재귀이니까 앞에서부터(ex [0][1]의 길이를 채워나가는 게아니라 뒤에서부터(ex [3][0]부터 거꾸로 채워나간다))
            '''
            순서가 0->1->2->3->0 이라고 할 ㄸ
            cache[2][111] = [3][0] + [2][3] 이고
            cache[1][11] = ([3][0] + [2][3]) + [1][2] 이고
            마지막으로
            cache[0][1] = ([3][0] + [2][3] + [1][2]) + [0][1] 이다
            '''
            #
            cache[last][visited] = tmp

            return tmp

    return find_path(0, 1 << 0)
