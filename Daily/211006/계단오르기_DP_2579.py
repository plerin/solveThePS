'''
GOAL : 규칙에 따라 계단 오르며 점수 최대 득점 리턴
1. 입력 받기
    1) S = 계단 개수
    2) SCORES(LIST) : 계단별 점수
DP 풀이법
    1) 동적 테이블 초기화 : 0이고 계단 개수만큼 
    2) 최적해 : ai = i만큼 오르며 얻을 수 있는 최대 값
    3) 점화식 
'''

S = int(input())
SCORES = []
for _ in range(S):
    SCORES.append(int(input()))

dp = [0] * S

dp[0] = SCORES[0]
dp[1] = SCORES[0] + SCORES[1]
dp[2] = max(SCORES[1] + SCORES[2],SCORES[0] + SCORES[2])

for i in range(3,S):
    dp[i] = max(dp[i-3]+SCORES[i-1]+SCORES[i], dp[i-2]+SCORES[i])

print(dp[S-1])