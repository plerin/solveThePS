'''
>> P
N이 3의 거듭제곱이라고 할 때 패턴 N은 N*N 정사각형 모양
N > 3 인 경우 가운데 공백인 (N/3) * (N/3) 정사각형을 N/3 패턴으로 둘러싼 형태

>> S
접근
1. N 크기만큼 빈칸을 갖는 정사각형 배열 만들기
2. 재귀 호출
    - 좌표를 입력하면 해당 좌표에 그리기(1번 블록을) 그렇게 키워가
    - *3을 곱한 값이 N이면 나가고 아니면 3배 키워서 재귀 호출

코드
1. 입력 값 받기
N = int(input())
2. 정사각형 배열 만들기
arr = [[' ' for _ in range(N)] for _ in range(N)]
3. 함수 호출
recursive(0, 0, 3)
4. 함수 선언
def recursive(x: int, y: int, size: int):
    if size == 3:
        arr[0][:3] = arr[2][:3] ['*'] * 3
        arr[1][:3] = ['*',' ','*']
    
    div3 = size // 3

    for i in range(x,size,div3):
        for j in range(y, size, div3):
            if i == div3 and j == div3:
                continue
            for k in range(div3):
                arr[i+k][j:j+k] = arr[k][:div3]

    if size == N:
        return
    
    recursive(x, y, size * 3)
'''


def recursive(x: int, y: int, size: int):
    if size == 3:
        arr[0][:3] = arr[2][:3] = ['*'] * 3
        arr[1][:3] = ['*', ' ', '*']

    # 9등분 하기 위함
    div3 = size // 3

    for i in range(x, size, div3):
        for j in range(y, size, div3):
            # 가운데 공백 만들기
            if i == div3 and j == div3:
                continue
            # 해당 파트 1파트로 채우기
            for k in range(div3):
                arr[i+k][j:j+div3] = arr[k][:div3]

    if size == N:   # base_condition
        return

    # N로 키워가며 재귀 호출
    recursive(x, y, size * 3)


N = int(input())

arr = [[' ' for _ in range(N)] for _ in range(N)]

recursive(0, 0, 3)

for row in arr:
    print(*row, sep='')
