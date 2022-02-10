'''
>> P
N명(1~N-1) 중 주어진 친구 관계가 존재하는지 여부 확인 후 결과 출력
    - 존재하면 1 // 안하면 0 출력
    - N = 정점 수 // M = 간선 수 
>> S
관계를 이어보면 DFS가 적절해
    -> 간선 정보를 통해 해당 정점의 연결 노드를 GRAPH로 만들어
    -> 재귀 타고 들어갔을 때 중복없는 친구가 5명 모이면 가능한 것!
DFS를 재귀로 풀어가나
    -> BASE_CONDITION : LEN(5) -> RETURN TRUE 그 외는 모두 FALSE


연결 노드 리스트를 통해서 부분 수열을 구하는 문제었네!

1. 입력 값 변수 생성 + 방문 처리 변수(visited:list) 
2. 재귀함수
    - param : person(int) _ 친구 관계 알아볼 사람, friend(list) _ 친구 목록
    - logic
        1) bc : len(friend) == 5 then return True
        2) relatino(person) 탐색하며 friend목록에 없으면 추가
        3) if a == True -> return True return 
'''


def dfs(person: int, depth: int):
    if depth == 5:
        return True

    ret = False
    for i in relation[person]:
        if not visited[i]:
            visited[i] = True
            ret = dfs(i, depth+1)
            visited[i] = False
        # if i not in friend:
        #     friend.append(i)
        #     ret = dfs(i, friend)
        #     friend.pop()
            if ret == True:
                return True

    return False


N, M = map(int, input().split())
relation = [[] for _ in range(N)]
visited = [False] * N

for i in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

exist = False

for i in range(N):
    visited[i] = True
    if dfs(i, 1):
        exist = True
        break
    visited[i] = False
    # if dfs(i, [i]):
    #     exist = True
    #     break

# print(0)
if exist:
    print(1)
else:
    print(0)
