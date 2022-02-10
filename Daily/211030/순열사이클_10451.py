'''
[P]
1부터 N까지 정수 N개로 주어진 순열, 인덱스와 매칭하여 방향그래프 생성 , 순열 사이클 개수 구하기
[S]
커넥티드 컴포넌트 유형처럼 인접 노드에 접근해 방문처리해서 연결된 그룹(사이클) 구하기
    - 유형 : BFS / DFS
[L]
DFS
1. 입력 받기
    - T(int) : 테스트 개수
    - N(int) : 순열 크기
    - graph(list) : index와 매칭해서 연결 노드 방향성 있게 만들어
2. 추가 변수 선언
    - visited(list) : 방문 처리를 위한 리스트로 graph 크기 만큼 False로 생성 _ 방문 처리 : False -> True
3. graph를 돌며 함수 호출
4. 함수 선언(DFS)
    - 목적 : 인접 노드 돌며 사이클 찾고 반환 
    - PARAM : v(int) _ 현재 값  // visited(list) : 방문 확인
    - LOGIC :
        1) 기저 조건 : 따로 필요 없는게 방문처리를 해서 False 인 경우만 로직 수행
        2) 인접 노드를 돌며 방문 처리
    - return : True(사이클 찾았으면) / False(이미 방문처리 된경우)
5. 결과 출력
'''

from collections import deque


def find_cycle(v):
    # if visited[v] == True:
    #     return False

    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            find_cycle(i)

    return True


# def find_cycle(v):
#     queue = deque([v])

#     while queue:
#         v = queue.popleft()
#         visited[v] = True

#         for i in graph[v]:
#             if visited[i] == False:
#                 queue.append(i)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(len(arr)+1)]
    visited = [False] * (len(arr)+1)

    ret = 0

    for i in range(len(arr)):
        graph[i+1].append(arr[i])

    for i in range(1, n+1):
        if visited[i] == False:
            find_cycle(i)
            ret += 1

    print(ret)
