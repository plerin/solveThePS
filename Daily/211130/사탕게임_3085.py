'''
사탕게임
n*n 크기 사탕 채워넣고
인접한 두 칸을 골라 자리를 바꾼다
가장 긴 연속 부분 행/열의 값을 구한다

브루트 포스
[i][j]
1. [i][j]와 [i][j+1] 자리 바꾸기
    - 어떻게? [i][j+1]과 
2. 판단
2. [i][j]와 [i+1][j] 자리 바꾸기
2. 판단
'''


def search(arr: list):
    global ans

    for i in range(len(arr)):
        cnt = 1
        for j in range(1, len(arr)):
            if arr[i][j-1] == arr[i][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

        cnt = 1
        for j in range(1, len(arr)):
            if arr[j-1][i] == arr[j][i]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1


N = int(input())
candidate = [list(map(str, input())) for _ in range(N)]
ans = 1

for i in range(N):
    for j in range(N-1):
        # 인접 열 바꾸기(본인과 오른쪽)
        candidate[i][j], candidate[i][j+1] = candidate[i][j+1], candidate[i][j]
        search(candidate)
        candidate[i][j], candidate[i][j+1] = candidate[i][j+1], candidate[i][j]

        # 인접 행 바꾸기(본인과 아래)
        candidate[j][i], candidate[j+1][i] = candidate[j+1][i], candidate[j][i]
        search(candidate)
        candidate[j][i], candidate[j+1][i] = candidate[j+1][i], candidate[j][i]

print(ans)
