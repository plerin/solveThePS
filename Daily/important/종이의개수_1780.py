'''
>> P
N*N 행렬에 3가지 종이(-1, 1, 0)이 있는데 조건에 따라 자르려고 한다.
각 종이로 채워진 종이 개수를 구하라
    - 조건
        1) 종이가 모두 같은 수로 되어 있으면 그대로 사용
        2) (1)이 아닌 경우 9개로 자르고 1을 판단
>> S
분할 정복이 이진 탐색이랑 같다고 봤는데 다르구나
큰 문제를 해결할 수 있는 작은 문제로 나눈 뒤 해결

접근
1. 종이가 모든 같은 수로 이루어져있는가 판단
2. 같은 크기의 종이 9개로 자르고 다시 1번 판단 수행
3. 그 과정에서 모두 수행된 뒤 선택된 원소의 값을 카운트

코드
1. 입력 받기
N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

2. 변수 선언 및 함수 호출
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0
check(0,0,N) # [0][0]좌표 & 행렬 크기

3. 함수 선언
def check(row: int, col: int, size: int) -> None:
    global cnt 3개
    pick = paper[row][col]

    for i in range(row, row+size):
        for j in range(col, col+size):
            if paper[i][j] != pick:
                n_size = size // 3
                # 작은 3*3 재귀 호출
                return

    if pick == [-1/0/1]에 따라 cnt += 1

4. 결과 출력
'''
import sys

input = sys.stdin.readline


def check(row: int, col: int, size: int) -> None:
    global cnt

    pick = paper[row][col]  # 지정된 숫자

    for i in range(row, row+size):
        for j in range(col, col+size):
            if paper[i][j] != pick:         # 2번 조건 해당 == 모두 같은 숫자가 아닌 경우
                n_size = size // 3

                # 작은 9개 사각형으로 나눠 진행 _ 큰 사각형을 작은 사각형으로 나눈다 == 분할 정복
                check(row, col, n_size)
                check(row, col+n_size, n_size)
                check(row, col+n_size*2, n_size)
                check(row+n_size, col, n_size)
                check(row+n_size, col+n_size, n_size)
                check(row+n_size, col+n_size*2, n_size)
                check(row+n_size*2, col, n_size)
                check(row+n_size*2, col+n_size, n_size)
                check(row+n_size*2, col+n_size*2, n_size)
                return

    cnt[pick+1] += 1    # 1번 조건 해당 == 모두 같은 숫자인 경우


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0, 0]  # [-1, 0, 1] 순서대로 초기값 입력

check(0, 0, N)  # [0][0], 크기 N부터 시작

print(*cnt, sep="\n")
