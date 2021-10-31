'''
[P]
1번부터 N번까지 도시를 순회하고 출발 도시로 돌아오는데 가장 적은 비용을 구하라
    - 도시 간 비용이 다르다(갈 때/올 때)
    - 길이 없을 수도 있다([x][y] = 0)
[S]
외판원 문제 => 완전탐색 / DFS&BFS / 다이나믹프로그래밍
    - 여기선 DFS로 풀어보려 함 _ 다시 출발도시로 돌아와야 하니까 시작 도시는 의미 없음 == 어느 노드에서건 출발 가능
[L]
1. 입력 받기
    - N(int) : 도시 수
    - graph(list) : 도시 간 길 비용 _ [i][j] = 도시 i에서 j 가는데 소요 비용
2. dfs 함수 호출
3. dfs 함수 선언
    - 목적 : 재귀호출하며 모든 경로에 해당하는 비용 중 가장 적은 비용 리턴
    - param
        1) p_city(int) : 현재도시
        2) n_city(int) : 다음도시
        3) cost(int) : 누적 비용
        4) visited(list) : 누적 도시
    - logic
        1) 기저조건 : len(visited) == N then return cost
        2) 인접 도시 찾아 재귀 호출(return)
        3) 
    - return : 최초 호출 시 재귀 함수 호출 끝나고 가장 작은 값 리턴
4. 결과 출력


1. 모든 도시를 순회하고 출발 도시로 돌아와 == 출발 도시는 상관없음
2. 길이 있는 모든 노드를 순회해 
    - 노드를 들릴 때 마다 visited에 담고 그 방면으로 순회가 끝나면 다시 visited에서 제외(빼)
3. 기저조건 : visited len()이 N-1개일 때 다음 도시들렸다가 반환하는 cost + graph[마지막도시][출발도시]
4.
    - 
'''


import sys


# def dfs(start: int, cost: int, visited: list):
#     if len(visited) == N:
#         if graph[start][0] != 0:
#             ret.append(cost+graph[start][0])
#         return

#     for i in range(1, N):
#         if i not in visited and graph[start][i] != 0:
#             visited.append(i)
#             dfs(i, cost+graph[start][i], visited)
#             visited.pop()
#             # print(visited, c+graph[i][0])

#     return False


# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# visited = [0]
# ret = []

# dfs(0, 0, visited)
# print(min(ret))


input = sys.stdin.readline


def dfs(start: int, next: int, cost: int, visited: list):
    global min_value

    if len(visited) == N:
        if graph[next][start] != 0:
            min_value = min(min_value, cost+graph[next][start])
        return

    for i in range(N):
        if i not in visited and graph[next][i] != 0 and start != i:
            visited.append(i)
            dfs(start, i, cost+graph[next][i], visited)
            visited.pop()


if __name__ == '__main__':

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    min_value = sys.maxsize

    dfs(0, 0, 0, [0])
    # for i in range(N):
    #     dfs(i, i, 0, [i])

    print(min_value)
