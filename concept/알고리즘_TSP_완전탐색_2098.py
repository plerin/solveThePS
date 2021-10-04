'''
완전 탐색을 활용한 TSP 알고리즘 코드 작성
시간 복잡도 : O(N!)
모든 도시를 출발지로 설정하고 그 도시에서 모든 도시를 살펴보는 기능 수행
'''

# 외판원 알고리즘 _ D : 비용 행렬


def tsp(D):
    N = len(D)
    inf = float('inf')  # 무한 값
    ans = inf
    VISITED_ALL = (1 << N) - 1  # N비트 모두 켜기 _ EX) 4 => 1111

    # start = 시작 도시 / last 중간 경로의 마지막 방문 도시 / visited : 방문 도시 집합 / tmp_dist : 중간 경로의 길이
    def find_path(start, last, visited, tmp_dist):
        nonlocal ans    # tsp의 변수 의미
        if visited == VISITED_ALL:
            return_home_dist = D[last][start] or inf
            ans = min(ans, tmp_dist + return_home_dist)
            return

        for city in range(N):
            # city 방문 하지 않았고(비트 마스크) // 도시간 연결되어 있으면
            if visited & (1 << city) == 0 and D[last][city] != 0:
                find_path(start, city, visited | (
                    1 << city), tmp_dist+D[last][city])

    # 0부터 n-1까지 모든 노드에서 출발해서 가장 작은 값 구하기
    for c in range(N):
        find_path(c, c, 1 << c, 0)

    return ans
