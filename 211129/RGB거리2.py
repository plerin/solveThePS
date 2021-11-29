'''
3*n 거리에서 R/G/B 중 비용이 작은걸로 새길해 최소 비용을 구하고자 함
    - 1,N 색이 같지 않아야 한다
    - 2~N-1 에는 i-1 / i+1 집의 색과 달라야 한다

한 줄을 추가했을 때 경우의 수는
R 선택 / G 선택 / B 선택 총 3가지 ==> 이에 따른 최적해 계산하자

a[i][j] => i = 순서 // j[0] = R선택 & j[1] = G선택 & j[2] = B선택
점화식
    a[i][0] = min(a[i-1][1], a[i-1][2])
    a[i][1] = min(a[i-1][0], a[i-1][2]) ...
    단, a[1] = [26,40,83] 으로 초기화
    ++ 마지막 리턴 하기전에(return min(dp[n]) 1번째 순서 찾아서 제외
'''


def findSmallestVal(num: int, house: list):
    dp = [[0 for _ in range(3)] for _ in range(num)]

    ans = int(1e9)
    for i in range(3):
        for j in range(3):
            if i == j:
                dp[0][j] = house[0][i]
            else:
                dp[0][j] = int(1e9)
        # dp[0] = [house[0][i], house[0][i], house[0][i]]
        # print(dp)
        for j in range(1, num):
            dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + house[j][0]
            dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + house[j][1]
            dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + house[j][2]

            # if j == num-1:
            #     dp[j][i] = int(1e9)
        # print(i, ' : ', dp)
        for j in range(3):
            if i == j:
                continue

            ans = min(ans, dp[num-1][j])

            # else:
            #     dp[0][j] = int(1e9)

    return ans


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

ret = findSmallestVal(N, house)

print(ret)
