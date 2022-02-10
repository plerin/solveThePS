'''
>> P
이전 숨바꼭질 문제와 같은데 추가된 사항이 하나 있어
    - 경로까지 표출하기
>> S
경로를 표출하려면 어떻게 해야해?
    - queue에 x좌표 넣을 때 현재까지의 경로도 같이 넣어준다면?
        -> 정답인데 시간초과 아무래도 10만에서 str을 누적하면 무리인가봐
        -> 비트마스크 써보는거 어때?  1 | 1 << 1이면 너무 크니까 숫자마다 [0]를 MAX만큼 갖고있고 
    - nx가 K면 return 경로 하고 그걸 그대로 표출

접근방법
어떤 방법으로 이동해도(+1 / -1 / *2)
각 위치에서의 최소의 소요 값만 저장하기
'''
from collections import deque

MAX = 30


def find_younger(older: int):
    global visit

    if N == K:
        return str(N)

    queue = deque([(older, str(older))])
    visit[older] = True

    while queue:
        x, route = queue.popleft()

        for i in range(3):
            nx = eval(str(x)+dx[i])

            if 0 <= nx < MAX and not visit[nx]:
                visit[nx] = True
                next_route = route+' '+str(nx)
                queue.append((nx, next_route))

                if nx == K:
                    return next_route
        visit[x] = False


N, K = map(int, input().split())
visit = [False] * MAX
dx = ['+1', '-1', '*2']

ans = find_younger(N)
# print(visit)
print(len(ans.split())-1, ans, sep="\n")
