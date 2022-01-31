'''
>> P
예제를 보고 규칙을 유추한 뒤 별을 찍어보시오
    - N은 항상 3*2**k이다 
>> S
이 문제도 N만큼 2차원 배열을 디폴트(' ')로 만들어 놓고 규칙에 따라 '*' 그리기
N == 1 부터 시작 -> k가 커질 수록 반복되는 패턴
좌표를 지정하고 거기에 N == 1 일때 삼각형을 그리는건 어떨까?

접근
N > 3인 경우부터 좌표를 지정하여 n=1일 때 를 그리기
if N == 3 then 하나 그리고 끝
else 3개 그리는 재귀 호출 ( size는 //2로 줄여나가기)

코드
1. 입력 받기
N = int(input())
2. 2차원 배열 초기화(디폴트 ' ')
arr = [[' ' for _ in range(2*N)] for _ in range(N)]
3. 함수 호출
    - param : 좌표(x, y), size(N)
recursive(0, N-1, N)
4. 메소드 
def recursive(x: int, y: int, size: int) -> None:
    if size == 3:
        arr[x][y] = '*'
        arr[x+1][y-1] = arr[x+1][y+1] = '*'
        for i in range(-2,3):
            arr[x+2][y+i] = '*'
    else:
        recursive(x, y, size//2)
        recursive(x+3, y-3, size//2)
        recursive(x+3, y+3, size//2)
'''

# size == 3일 때와 size == 6일 때가 다르고 이 패턴의 경우 size == 6(3*2)일 때의 패턴!
# 좌표를 주고 해당 좌표에 가장 작은 삼각형을 그리는 문제


def recursive(x: int, y: int, size: int) -> None:
    if size == 3:
        arr[x][y] = '*'
        arr[x+1][y-1] = arr[x+1][y+1] = '*'
        for i in range(-2, 3):
            arr[x+2][y+i] = '*'
    else:
        n_size = size // 2
        recursive(x, y, n_size)
        recursive(x+n_size, y-n_size, n_size)
        recursive(x+n_size, y+n_size, n_size)


N = int(input())

# 가로가보다 열이 2배 더 길어 == 2*N
arr = [[' ' for _ in range(2*N)] for _ in range(N)]

recursive(0, N-1, N)

for row in arr:
    print(*row, sep='')
