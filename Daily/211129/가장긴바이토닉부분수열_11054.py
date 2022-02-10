'''
ai = i길이 수열에서 가장 긴 바이토닉 수열 길이 최적해
양방향(ltor, rtol)으로 증가 부분 수열을 각 자리마다 구하고 그 합 중 큰 값을 반환
if 양방향 값 모두 0이 아닌경우 -1(해당 순서 숫자 중복)

a[i][j] -> i = 순서 // j[0] = ltor 부분증가길이, j[1] = rtol 부분증길이 최적해

ltor 부분 증가 길이 최적 해 점화식
ai = max(ai, aj + 1) j는 0부터 i-1까지 반복 & ai는 1로 초기화

'''


def solve(n: int, seq: list):
    dp = [[1 for i in range(2)] for _ in range(n+1)]

    # n = 3
    for i in range(1, n+1):  # 1,2,3
        for j in range(1, i):  # 1 , 1, 2
            if seq[i] > seq[j]:
                dp[i][0] = max(dp[i][0], dp[j][0]+1)
        for k in range(1, i):  # 3 , 3, 2
            if seq[(n+1)-i] > seq[(n+1)-k]:
                dp[(n+1)-i][1] = max(dp[(n+1)-i][1], dp[(n+1)-k][1]+1)

    max_val = 0
    for i in range(1, n+1):
        max_val = max(max_val, sum(dp[i]))

    return max_val-1


N = int(input())
seq = [0] + list(map(int, input().split()))

ret = solve(N, seq)

print(ret)
