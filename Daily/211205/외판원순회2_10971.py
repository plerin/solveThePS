'''
1~N개의 도시가 있고 도시를 잇는 길이 있다.
한 도시에서 출발해 N개 도시를 모두 거쳐 다시 원래 도시로 돌아오는 여행하는데 최소 비용
    - a -> b 비용과 b -> a 비용이 다를 수 있다.
    - 도시 간 이동 할 수 없는 경우 0이다.

풀이
재귀(dfs) 풀이해보자
2차원 배열(도시간 비용이 나와있는 행렬)
    - param : visit(list) _ 현재까지 여행한 도시, cost(int) _ 현재까지 비용
    - vari : global N(int), graph(list),  distance(list) _ 도시 수 / 도시간 이동 비용 / 도시 간 연결 도시
    - logic
        1) base_condition : if len(visit) == N then cost + graph[visit[-1]][visit[0]]
        2) for i in range(1,N+1):
            if i not visit then recur(visit.append(i), cost+gra)
'''


def getMinimumCost(start: int, visit: list, cost: int):
    global N, ans, graph

    if len(visit) == N:
        if graph[visit[-1]][start] != 0:
            ans = min(ans, cost + graph[visit[-1]][start])
        return

    for city in range(N):
        if city in visit or graph[visit[-1]][city] == 0 or city == start:
            continue
        cost += graph[visit[-1]][city]
        visit.append(city)
        getMinimumCost(start, visit, cost)
        visit.pop()


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = int(1e9)

for i in range(N):
    getMinimumCost(i, [i], 0)
print(ans)
