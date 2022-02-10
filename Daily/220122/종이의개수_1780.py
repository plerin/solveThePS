'''
>> P
N*N 종이가 있고 3가지 숫자가 저장되있을 때
규칙에 다라 적절한 크기로 자르고 각 숫자가 채워진 종이 개수를 구하라
    - 숫자 : -1 / 0 / 1
    - 규칙
        1) 종이가 모두 같은 수라면 그대로 사용
        2) 1번 조건이 아닌 경우 같은 크기 종이 9개로 자르고 1규칙을 다시 판단
>> S
큰 종이를 작게 자르며 조건에 만족하는지 판단 
=> 분할정복(divide and conquer)

접근
1. 시작점의 숫자를 저장
2. 행렬을 탐색하며 같은 숫자인지 판단
    1) 같은 숫자 -> 해당 숫자 += 1(결과 값)
    2) 같은 숫자가 아니라면 -> 작은 사각형으로 분할(9개) -> 재탐색(재귀호출)
3. 결과 출력

코딩
1. 입력 받기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
2. 변수 선언
ans = [0, 0, 0] _ 결과 값(종이에 따른 카운트) [-1, 0, 1] 에서 + 1씩함
3. 함수 호출
get_count(0, 0, N)

def get_count(row, col, size):
    global ans
    pick = paper[row][col]
    
    for i in range(row, row+size):
        for j in range(col, col+size):
            if pick != paper[i][j]:
                n_size = size // 3
                
                9가지 크기 사각형으로 재귀 호출
                return
    ans[pick+1] += 1
4. 결과 출력

'''

import sys

input = sys.stdin.readline


def get_count(row: int, col: int, size: int) -> None:
    global result

    pick = paper[row][col]

    for i in range(row, row+size):
        for j in range(col, col+size):
            if pick != paper[i][j]:
                n_size = size // 3

                for ii in range(3):
                    for jj in range(3):
                        get_count(row + (n_size*ii), col + (n_size*jj), n_size)
                # get_count(row, col, n_size)
                # get_count(row, col + n_size, n_size)
                # get_count(row, col + (n_size*2), n_size)
                # get_count(row + n_size, col, n_size)
                # get_count(row + n_size, col + n_size, n_size)
                # get_count(row + n_size, col + (n_size*2), n_size)
                # get_count(row + (n_size*2), col, n_size)
                # get_count(row + (n_size*2), col + n_size, n_size)
                # get_count(row + (n_size*2), col + (n_size*2), n_size)
                return

    result[pick+1] += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0, 0]

get_count(0, 0, N)

print(*result, sep='\n')
