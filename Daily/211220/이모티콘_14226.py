'''
>> P
1개 이모티콘을 복붙해서 S개를 만드려고 할 때 시간의 최솟값을 구하라
    - 1초 소요 : 복사 / 붙여넣기 / 1개 삭제
    - 일부만 선택 불가
>> S
복사 + 붙여넣기(2초)가 지나야 기존 개수가 2배가 된다. 
    - [S] = 최소 소요 시간 저장 

>> F
def minimum_time(cnt: int)
    - vari : during_time(list_global) _ S개수만큼 -1으로 초기화, sec(int) _ 시간 흘러감
    - logic :
        1) declare queue(deque) & init during_time[cnt] = 0 
        2) while queue & cnt = queue.popleft() & cnt += 1
        3) if cnt % 2 == 0 then *2 , -1 if time[cnt] == -1 then initial
'''

from collections import deque

MAX = 1001


def minimum_time(cnt: int):
    global d_time

    queue = deque([])
    # queue.append(cnt)
    queue.append(cnt)
    d_time[cnt] = 0
    sec = 1

    while queue:
        cnt = queue.popleft()

        if sec % 2 == 0:
            nx = eval(str(cnt)+'*2')
            # print(nx)
            if nx < MAX and d_time[nx] == -1:
                d_time[nx] = sec
                queue.append(nx)
        else:
            queue.append(cnt)

        nx = eval(str(cnt)+'-1')
        if 0 <= nx and d_time[nx] == -1:
            d_time[nx] = sec
            queue.append(nx)

        sec += 1


S = int(input())
d_time = [-1] * MAX

minimum_time(1)

print(d_time[S])
