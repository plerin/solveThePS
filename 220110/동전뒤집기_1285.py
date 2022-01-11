'''
>> P
N*N 행렬에서 동전을 뒤집어 뒷면이 최소 개수인 경우 구하라
    - 동전 : H(앞면) / T(뒷면)
    - 행동 : row / column 전체 뒤집기
>> S
행동 조건이 룰을 찾아 최소의 경우를 구하는 문제 == 그리디 알고리즘


풀이법
모든 경우의 수를 다 해보면서 최소 값을 구하는 것
행마다 경우의 수는 뒤집는다 / 안 뒤집느다 == 2가지
    - 3행이면 모든 경우의 수는 2**3 == 8가지
경우의 수(== 뒤집는)가 끝날 때마다 열을 탐색하며 뒷면(T) 개수를 파악
만약 'T'의 개수가 'H'보다 더 많으면 N-T의 개수를 tot에 구한다
    - 뒷면이 더 많다 == 뒤집고 난 뒤 T의 개수를 더한다
    -> tot += min(cnt, N-cnt)


'''

n = int(input())
coin = [list(input()) for _ in range(n)]
ans = n * n + 1  # 입력 값중 최대 값

for bit in range(1 << n):   # 모든 경우의 수 만큼 반복 _ 각 행마다 2가지 경우(뒤집는다 / 안뒤집는다) => 2 ** n가지
    tmp = [coin[i][:] for i in range(n)]    # 입력 값(본래) 불러옴
    for i in range(n):  # 동전 개수만큼 반복
        if bit & (1 << n):  # 현재 경우의 수가 몇 개의 row을 포함하는지(==뒤집는지)
            for j in range(n):
                if tmp[i][j] == 'H':
                    tmp[i][j] = 'T'
                else:
                    tmp[i][j] = 'H'
    tot = 0  # n*n 행렬에서 뒷면 개수
    for i in range(n):
        cnt = 0
        for j in range(n):
            if tmp[i][j] == 'T':
                cnt += 1
        # 열에서 'T'개수가 'H'보다 적으면 n-cnt(다 뒤집은)경우를 더해줘 _ 최솟값을 구하는것이기 때문
        tot += min(cnt, n-cnt)
    ans = min(tot, ans)

print(ans)
