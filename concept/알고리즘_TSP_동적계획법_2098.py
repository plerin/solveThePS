'''

동적 계획법 => 알고리즘 시간 복잡도 == 캐시의 크기
사이클은 그래프에서 매우 중요한 개념 중 하나로 일반적인 개념으로는 첫 정점과 마지막 정점이 중복되는
경로로 이를 통해 경로를 무한히 순회할 수 있다. => 이 경로를 만들 수 있으면 시작점은 중요하지 않다
1번이든 2,3,4번 시작이든 정답 경로는 반드시 숧게 되어 있고 결국 시작점을 단일 도시로 고정해도
정답 경로를 지나치게 돼서 시작 ㄱ도시를 추적하지 않아도 된다.

중복 호출되는지 확인해야한다 이것이 확인되어야 동적 계획법이 실효성을 갖는다.

완전 탐색을 활용한 TSP 알고리즘 코드 작성
시간 복잡도 : O(N*2**n)
cache에 중간 과정을 저장해두고 중복 호출될 경우 바로 사용하여 시간 복잡도를 줄이는 것이 핵심
'''


def tsp(dists):
    N = len(dists)
    VISITED_ALL = (1 << N)-1
    cache = [[None] * (1 << N) for _ in range(N)]  # cache 크기 == 동적 계획법의 시간복잡도
    INF = float('inf')

    def find_path(last, visited):
        if visited == VISITED_ALL:
            return dists[last][0] or INF

        if cache[last][visited] is not None:
            return cache[last][visited]

        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 or dists[last][city] != 0:
                tmp = min(tmp, find_path(city, visited |
                                         (1 << city))+dists[last][city])
        cache[last][visited] = tmp
        return tmp

    return find_path(0, 1 << 0)
