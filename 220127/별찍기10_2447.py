'''
>> P
N이 3의 거듭제곱이라 할 때, 크기 N의 패턴은 N*N 정사각형 모양이다.
N=3일 때 가운데 별이 하나 없는 패턴
N>3일 때 가운데 (N/3)*(N/3) 정사각형을 크기 N/3 패턴으로 둘러싼 형태

>> S
3의 거듭제곱 형태인데 N>3인경우 /3으로 나눠가며 진행
-> 9파트로 나눠(가운데는 뻥 뚫린) 그리고 5번째 파트와 나머지 파트로 구분
if part == 5 then (N/3)*(N/3) 2차원배열을 빈칸으로만
if part != 5 then 다시 /3으로 나눠 똑같이 진행 

2차원 배열 만들어 놓고 재귀로 해당 인덱스 찾아가며 채우기 *이냐 ' '이냐

MAX = 3**N+1

base_condition
if size == 3
    if (row/3) % 3 == 0 and (col/3) % 3 == 0:
        continue
    else:
        for i in range(row, row+size):
            for j in range(col, col+size):
                if i == row+1 and j == col+1:
                    continue
                arr[i][j] = '*'
    return

size /= 3

solve(row, col, size)
solve(row, col+size*1, size)
solve(row, col+size*2, size)

solve(row+size*1, col, size)
solve(row+size*1, col+size*2, size)

solve(row+size*2, col, size)
solve(row+size*2, col+size*1, size)
solve(row+size*2, col+size*2, size)

'''


def solve(row: int, col: int, size: int):
    global arr

    if size == 3:
        for i in range(row, row+size):
            for j in range(col, col+size):
                if i == row+1 and j == col+1:
                    continue
                arr[i][j] = '*'
        return

    size //= 3

    solve(row, col, size)
    solve(row, col+size*1, size)
    solve(row, col+size*2, size)

    solve(row+size*1, col, size)
    solve(row+size*1, col+size*2, size)

    solve(row+size*2, col, size)
    solve(row+size*2, col+size*1, size)
    solve(row+size*2, col+size*2, size)


N = int(input())
arr = [[' ' for _ in range(N)] for _ in range(N)]

# print(arr)

solve(0, 0, N)


for row in arr:
    print(*row, sep='')
