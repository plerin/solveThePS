'''
>> P
0과 1로만 이루어진 행렬 A,B, A->B 바꾸는데 필요한 연산 최솟값 구하라
    - 변환 연산 : 3*3 모든 원소 뒤집기(0<->1)
>> S
규칙 찾기 
순서대로(row -> col) 탐색하다가 A와 B가 다른 원소를 만나면 해당 좌표에서 (x+3,y+3)으로 행렬을 바꿔 
    - 만약 x, y 모두 +3 좌표가 범위를 벗어난 경우 continue or break

1. 입력받는다. _ matrix_a, matrix_b
2. 함수 호출
ans = solve()
def solve():
    global matrix_a, matrix_b
    ret = -1
    
    for i in range(N):
        for j in range(M):
            if mat_a[i] != mat_b[i]:
                # 범위나가면 continue
                if change(i, j)
    return ret 
3. 결과 출력
'''


def isin(x, y):
    for i in range(1, 3):
        if x + i == N or y + i == M:
            return False
    return True


def change(x, y):
    global matrix_a

    for i in range(x, x+3):
        for j in range(y, y+3):
            # matrix_a[i][j] = 0 if matrix_a[i][j] == 1 else 1
            matrix_a[i][j] = 1 - matrix_a  # 0과 1을 toggle하는 신박한 방법

    return True


def solve():
    global matrix_a, matrix_b
    ret = 0
    # N-2, M-2만 반복하면 isin()사용할 필요 없음 어짜피 마지막에 A==B로 판별하니까!
    for i in range(N):
        for j in range(M):
            if matrix_a[i][j] != matrix_b[i][j]:
                if isin(i, j) and change(i, j):
                    ret += 1

    return ret


N, M = map(int, input().split())
matrix_a = [list(map(int, input())) for _ in range(N)]
matrix_b = [list(map(int, input())) for _ in range(N)]

ans = solve()

print(ans if matrix_a == matrix_b else -1)
