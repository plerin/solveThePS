'''
[P]
8*8 좌표 평면에서 나이트 이동할 수 있는 경우의 수 
    - 수평으로 두 칸 이동한 뒤 수직으로 한 칸 이동
    - 수직으로 두 칸 이동한 뒤 수평으로 한 칸 이동
[S]
구현(implementation) 중 시뮬레이션 유형

[L]
1. 변수 선언
    1) start(str) _ 입력 값 _ 시작 위치(열*행)
    2) cols(dic) _ 문자로 되어있는 열을 숫자로 매칭 _ cols = {'a':1, 'b':2 ..., 'h':8}
    3) dx,dy(list) _ 방향벡터, 나이트가 움직일 수 있는 경우의 수
2. 시작 위치 형식 변환
    1) 문자로 이뤄진 시작점을 이중배열 형태(숫자)로 변환 -> (x,y)
2. 함수 이용
    1) PARAM : start(tuple) _ (x,y)
    2) LOGIC :
        1_ 방향벡터(dx/dy) 크기만큼 반복하며 좌표8*8)을 넘은 경우 continue
        2) cnt += 1
    3) RETURN : cnt
'''


def moveKnight(str):
    cnt = 0
    for i in range(len(dx)):
        nx, ny = str[0]+dx[i], str[1]+dy[i]

        if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
            continue
        cnt += 1

    return cnt


start = input()
cols = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
dx, dy = [-1, -1, 1, 1, -2, -2, 2, 2], [2, -2, 2, -2, 1, -1, 1, -1]

conv_str = (int(start[1]), cols[start[0]])

ret = moveKnight(conv_str)

print(ret)


def moveKnight2(str):
    cnt = 0
    for step in steps:
        nx, ny = str[0]+step[0], str[1]+step[1]

        if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
            continue
        cnt += 1

    return cnt


start = input()
# cols = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]

conv_str = (int(start[1]), int(ord(start[0])) - int(ord('a')) + 1)

ret = moveKnight2(conv_str)

print(ret)
