
# dfs , bfs 모두 풀어볼 것

# dfs
'''
파라미터 : 시작 노드, visit list
종료조건 : 더 이상 재귀 호출 하지 않을 때
방문체크 : visited list에 해당 노드 추가
'''


from collections import deque


def dfs(s, visit=[]):
    visit.append(s)

    for i in graph[s]:
        if i not in visit:
            dfs(i)

    return visit


# bfs
'''
파라미터 : 시작 노드
변수 : 반환 리스트 
방문체크 : 노드 방문하며 반환 리스트 없는 경우만 q에 추가
'''


def bfs(s):
    c_lst = []
    q = deque([s])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if i not in c_lst:
                c_lst.append(i)
                q.append(i)
    return c_lst


# 노드 , 간선 입력받기
node = int(input())
edge = int(input())

graph = [[] for _ in range(node+1)]
# 그래프 만들기 [i][j] 와 [j][i]에 모두 값 넣기
for i in range(1, edge+1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# dfs/bfs 호출
ret = bfs(1)
print(ret)
print(len(ret)-1)

# 결과 출력
