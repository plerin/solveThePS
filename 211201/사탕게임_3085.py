'''
사탕게임
> P 
n*n에 4가지 사탕을 채워넣고 인접한 두 칸을 선택하여 교환했을 때 가장 긴 연속 부분 수열 찾기

kp
1. 인접한 두 칸을 교환하는 방법
    - 상/하/좌/우 교환할 수 있지만 n*n 행렬 모든 요소 반복한다면
    - 오른쪽(i+1 != n) / 아래(j+1 != n) 만 교환 그리고 다시 교환(제자리로)
    -> 오른쪽 교환 [i][j], [i][j+1] = [i][j+1], [i][j]
    -> 아래와 교환 [i][j], [i+1][j] = [i+1][j], [i][j]
2. 가장 긴 연속 부분(행/열) 찾는 방법
    - 모든 교환의 경우에 체크해야함 
    - 함수로 만들어 놓으면 편리함
    - n*n에 대해 행/열 체크 
    -> 행 체크 cnt = 1, if [i] == [i-1] cnt += 1  then ret = max(ret, cnt)
'''


def check(board: list):
    global ans, N

    for i in range(N):
        # 행 기준 체크
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        # 열 기준 체크
        cnt = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1


N = int(input())
board = [list(map(str, input())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        if j + 1 == N:
            continue
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        check(board)
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

    # for j in range(N):
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        check(board)
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(ans)
