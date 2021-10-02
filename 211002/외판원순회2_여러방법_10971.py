# 여러 방법이 있으니 모두 풀어보기
'''
>1. 순열로 경우의 수를 구하고 완전탐색
0. 라이브러리 선언, sys - 최대 값, 입력, itertools permutations - 순열 경우의 수
1. 입력 받기 _ n과 graph
2. 노드 값들로 순열을 만들어 최소 길이 구하기
3. 결과 출력
'''
# 0
import sys
from itertools import permutations

input = sys.stdin.readline
INF = sys.maxsize


def shortest_path(case):
    cost = 0
    for i in range(n-1):
        if graph[case[i]][case[i+1]] != 0:
            cost += graph[case[i]][case[i+1]]
        else:
            return False

    if graph[case[-1]][case[0]] != 0:  # 마지막에 다시 출발지로 돌아가는 길
        cost += graph[case[-1]][case[0]]
    else:
        return False

    return cost


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

n_num = [i for i in range(n)]  # 여기서의 핵심 노드를 리스트로 만들고 순열로 경우의 수 구함

ret = INF
for case in permutations(n_num):
    cost = shortest_path(case)
    if cost != False:
        ret = min(ret, cost)

print(ret)
