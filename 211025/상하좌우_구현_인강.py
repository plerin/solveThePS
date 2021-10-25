'''
[P]
N*N 크기의 공간(1*1 정사각형으로 나누어진)에서 여행가가 계획서 대로 움직인 위치 좌표를 반환하라
    - 왼쪽 위 좌표 = (1,1) // 오른쪽 아래 좌표 : (N,N)
    - 시작은 (1,1)
    - 상(U),하(D),좌(L),우(R) 로만 이동 가능
    - N*N 공간을 벗어나는 이동은 무시
[S]
구현(Implementation) _ 시뮬레이션 문제로 이차행렬 위 좌표이동
    - 계획서(UDRL) 각 이동에 해당하는 좌표 이동(해당 좌표가 N*N 안에 해당하는지 확인)
[L]
0. 변수
    - dir(dic) : 방향에 따른 x,y 좌표 이동 _ {'U':(-1,0)..}
1. 함수 이용
    - PARAM : plan(list) _ 입력으로 받은 계획서 내용
    - LOGIC :
        1. 출발 위치 지정 _ x,y = 0, 0
        2. loop with plan _ 루프를 돌며 위치 이동 -> if 변경된 좌표가 공간을 벗어나면 continue else x,y 갱신
        3. 결과 값 반환(x,y +=1)
    - RETURN : x,y _ 모두 +1씩 해줘, 출발지점이 (0,0)이 아닌 (1,1)이므로
'''


def moveCoord(plan):
    x, y = 0, 0

    for p in plan:
        nx, ny = x+dic[p][0], y+dic[p][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        x, y = nx, ny

    return x+1, y+1


N = int(input())
plan = input().split()
dic = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

ret = moveCoord(plan)

print(*ret)
