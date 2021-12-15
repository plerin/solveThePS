'''
>> P
1~N-1가 참가하는 캠프에 특정 관계 존재 여부 확인하는 프로그램 작성
    - N, M => 사람 수(정점), 관계 수(간선)
    - 존재하면 1, 없으면 0 출력
>> S
관계를 보면 5명이 중복되지 않으면 됨!
    -> N과 M에서 순열 찾던 문제와 비슷
입력 값에서 양방향 그래프로 친구 관계를 만들고(graph) DFS/BFS로 풀이하기
친구를 PARAM으로 하지 않고 전역변수로 TRUE/FALSE로 관계 나타내는 방법으로 풀어보자
    - fried = [False] * N (초기값) & 0~n-1 돌아보며 friend[i] = True // False
    - param : person(int), depth(int) 
    - logic :
        1) if depth == 5 then return True 
        2) for p in graph[person] -> if not friend[p] then friend[p] = True ret = dfs(p, depth+1)
            -> if ret == True then return True 
        3) default return False

'''
from collections import deque


def dfs(person: int, depth: int):
    if depth == 5:
        return True
    ret = False

    for p in graph[person]:
        if not friend[p]:
            friend[p] = True
            ret = dfs(p, depth+1)
            friend[p] = False

            if ret:
                return True

    return ret


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
friend = [False] * N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for p in range(N):
    friend[p] = True
    if dfs(p, 1):
        print(1)
        exit()
    friend[p] = False

print(0)
