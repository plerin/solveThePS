'''
> P
1~n 인원이 있는데 이 중 스타트/링크로 팀을 나눠 축구 경기하려고함
두 팀의 능력치 합의 차가 최소인 경우 출력하라
    - 팀은 적어도 1명 이상

> S
1. 팀 구성 만들기 _ COMBINATIONS _ 인원은 1~(N//2+1)
2. 팀 구성 별 능력치 합 구하기 
    - N으로 이중 반복문 -> 스타트/링크 팀 각각 합 구함
    - 차이 갱신 _ global ans 에 작은 값으로 갱신
3. 함수 만들기
    def devide_team(abil:list)
    - param : 능력치 리스트
    - vari : global N(int), ans(int) _ 정답 갱신 위함, start_team, link_team(list) _ 각 팀원
    - logic
        1) 팀 인원 가르기 1 ~ (n//2+1)
        2) combinations으로 팀 구분 
        3) 각 팀의 합 갱신
'''
from itertools import combinations

INF = int(1e9)


def devide_team(abil: list):
    global N, ans

    for num in range(1, N//2+1):
        for comb in combinations(range(N), num):
            start_team = comb
            link_team = list(set(range(N))-set(start_team))
            start_abil_sum, link_abil_sum = 0, 0

            for i in start_team:
                for j in start_team:
                    start_abil_sum += abil[i][j]

            for i in link_team:
                for j in link_team:
                    link_abil_sum += abil[i][j]

            # for i in range(N):
            #     for j in range(N):
            #         try:
            #             start_abil_sum += abil[start_team[i]][start_team[j]]
            #         except:
            #             start_abil_sum += 0
            #         try:
            #             link_abil_sum += abil[link_team[i]][link_team[j]]
            #         except:
            #             link_abil_sum += 0
            ans = min(ans, abs(start_abil_sum - link_abil_sum))


N = int(input())
abil = [list(map(int, input().split())) for _ in range(N)]
ans = INF

devide_team(abil)

print(ans)
