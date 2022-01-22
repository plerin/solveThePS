'''
>> P
2**N인 2차원 배열을 z모양으로 방문함
N, r행, c열을 몇 번째로 방문하는 지 출력
>> S
N 크기에 대해 규칙을 파악하여 풀이

N > 1 인 경우
2**n-1 * 2**n-1으로 4등분 한 뒤 재귀적으로 방문

접근
1. N == 1일 때와 N > 1일 때로 구분하여 로직 수행
2. if N > 1:
2**N-1 크기로 4등분 후 재귀순서 방문
n_size = 2**(N-1)
check(row, col, n_size, 0)
check(row, col+n_size, n_size, 1)
check(row+n_size, col, n_size, 2)
check(row+n_size, col+n_size, n_size, 3)

if i == r and j == c:
    n_size**n_size * part

코드
1. 입력 받기
N, r, c = map(int, input().split())
2. 변수 선언
3. 함수 호출
ans = solve((r, c), n)
4. 함수 선언
def solve(row, col, size):
    part = 0

    for i in range(row, row+)



N == 2
2*2 배열이 4개가 있는 경우 
배열 원소 크기만큼 늘어남
0, 4, 8, 12
N == 3 -> 0, 16, 
'''
