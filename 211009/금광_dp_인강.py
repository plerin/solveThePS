'''
goal : n*m 금광에서 얻을 수 있는 최대 금의 크기 출력
0. 라이브러리 추가 : 없음
1. 입력 받기 
    1) 테스트 횟수 : T
    2) 금광 : N*M
    3) 금광안의 금 : 한 줄 라인 -> gold 안에 이중배열로 담기
2. 로직 수행
    1) dp 테이블 초기화 : 이중배열 0으로 초기화
    2) [0]인경우 초기화
    3) n*m 루프돌며 dp 테이블 입력
    4) 출력
'''
# 1
# T = int(input())
# for _ in range(T):
#     n, m = map(int, input().split())
#     d = [[0]*m for _ in range(n)]
#     gold = []
#     row = []
#     for i, v in enumerate(list(map(int, input().split()))):
#         row.append(v)
#         if (i+1) % 4 == 0:
#             gold.append(row)
#             row = []
#     # d[0]인 경우 초기화
#     for i in range(n):
#         d[i][0] = gold[i][0]

#     for j in range(1, m):
#         for i in range(n):
#             d[i][j] = d[i][j-1]+gold[i][j]

#             if i-1 >= 0:
#                 d[i][j] = max(d[i][j], d[i-1][j-1]+gold[i][j])
#             if i+1 < n:
#                 d[i][j] = max(d[i][j], d[i+1][j-1]+gold[i][j])
#     print(max(list(zip(*d))[m-1]))

# 문제 풀이 답안 (조금 다른 방식 풀이)
for tc in range(int(input())):
    # 입력 받기 _ 금광정보
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # dp테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        # 다른 값이 아닌 주어진 값을 slicing 하여 초기화
        dp.append(array[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:  # i-1가 리스트에서 벗어나는 경우
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:  # i+1이 리스트에서 벗어나는 경우
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = max(left_down, left, left_up) + array[i][j]
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
