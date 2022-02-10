'''
goal : n명의 병사 중 규칙에 따라 배치하고 남아 있는 병사가 최대인 경우 반환
    1. 전투력 순으로 내림차순 정렬
    2. 앞은 뒤보다 무조건 커야함
    3. 열외 한 뒤 최대길이 만들기
1. 입력 받기
    1) N : 병사 수
    2) soldier(list) : 병사 수
2. 로직
    1) dp 테이블 초기화 : [0]으로 n+1개 초기화 _ 1~n에 해당 데이터 입력
    2) [0]인 경우 초기화
    3) 반복 수행
3. 결과 반환 _ d[n]
'''
# # 1
# N = int(input())
# soldier = list(map(int, input().split()))
# # 2
# d = [0] * (N)
# for i in range(1, N):
#     if soldier[i] >= soldier[i-1]:
#         d[i] = d[i-1]+1
#     else:
#         d[i] = d[i-1]
# # 3
# print(d[N-1])

# LIS(Longest Increasing Subsequence)를 활용한 풀이
N = int(input())
array = list(map(int, input().split()))

# 순서를 뒤집어 최장 증가 부분 수열_LIS 문제로 변환
array.reverse()

# DP 테이블 초기화 _ 0부터 시작하면 1개의 요소로 만들 수 있는 부분 수열 길이가 1이기에 1로 초기화
dp = [1] * N

for i in range(1, N):    # 0 == 1개 부분 수열 == 1(초기화 한 값) 그래서 1부터 시작
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))  # 우리가 구하고 싶은 건 열외 숫자니까 max(dp)를 뺌
