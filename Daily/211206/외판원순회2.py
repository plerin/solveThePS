'''
> P
외판원 순회 문제 : 1~N의 모든 도시를 들리고 마지막 도시에서 출발 도시로 돌아오는 최소 비용 구하라
    - 도시 간 이동 비용이 다르다(i->j 와 j->i)
    -> 순회하기 때문에 출발지는 상관 없다.

solve#1. 완전 탐색
1. 순회하기 때문에 출발점은 상관 없다(어느 출발점이든 같은 값이 나온다 -> 그림그려봐)
    -> 0에서 출발하도록 임의로 정해서 구하기

FUNCTION(move)
    - param : now(int) _ 현재 도시  // depth(int) _ 현재 누적 여행 도시
    - vari : global charge(int) _ 비용 누적 , global ans(int) _ 결과 저장
    - logic
        1) base_condition : if depth == n then if graph[now][0] != 0 then ans = min
        2) for i in range(len(graph)) -> if not visit[i] and graph[now][i] != 0 then visit[i] = True & charge += graph[now][i] 
        3) visit[i] = False & charge -= graph[now][i]

solve#2. 비트마스트 + DP
'''

# import sys

# input = sys.stdin.readline
# INF = int(1e9)


# def move(now: int, depth: int, charge: int):  # this parameter is only about recursive function
#     global ans, visit

#     if depth == N:
#         if graph[now][0] != 0:
#             ans = min(ans, charge + graph[now][0])
#         return

#     for l in link[now]:  # search about present associated city
#         if visit[l]:
#             continue
#         visit[now] = True
#         move(l, depth+1, charge + graph[now][l])
#         visit[now] = False


# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# link = [[] for _ in range(N)]
# visit = [False] * N
# ans = INF

# # gathering connected city by city
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] != 0:
#             link[i].append(j)

# move(0, 1, 0)   # now city, depth(visit city), charge

# print(ans)

# 방문 도시를 비트마스크로 저장 1110 -> 4,3,2 도시 방문 & 1 도시 방문 안함


def find(now: int, before: int):
    if before == (1 << n) - 1:
        return graph[now][0] if graph[now][0] != 0 else sys.maxsize

    if dp[now][before] != 0:
        return dp[now][before]

    cost = sys.maxsize
    for i in range(1, n):
        if not (before >> i) % 2 and graph[now][i]:
            tmp = find(i, before | (1 << i))  # i번째 도시 방문한다는 의미
            cost = min(cost, tmp + graph[now][i])
            dp[now][before] = cost
    return cost


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]

print(find(0, 1))
# print(dp)
