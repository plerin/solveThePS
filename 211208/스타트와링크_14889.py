'''
> P
n명이 있고 n/2명으로 짝지어 스타트 / 링크 팀을 이룬다 이 때 양 팀의 능력치 차가 최소인 경우
    - n은 짝수
    - 팀의 능력치(abillity) = 모든 쌍의 능력치 Sij의 합
        ex) 1,2,3 팀이면 S12 + S21 + S13 + S31 + S23 + S32 (N개 중 N개 순열?!)
        -> list(permutation(range(1,4),2)) 

> S
1. 팀을 나눈다
for comb in combination(range(N),N/2)
    start = set(comb)
    link = set(range(N)) - start
    
    diff = INF
    start_sum, link_sum = 0, 0

    for (i,j) in permutations(start,2):
        start_sum += abil[i][j]
    for (i,j) in permutations(link,2):
        link_sum += abil[i][j]

    diff = min(diff, abs(start_sum-link_sum))

func devide_team
    - param : ability(list) _ 입력 값 
    - vari : global N,ans(int) _ 총 인원 및 결과 , start,link(set) _ 팀 나누기, start_sum,link_sum(int) _ 팀 능력치 합
    - logic
        1) 팀을 나눈다 (start / link)
        2) 팀별 합을 구한다
        3) 가장 작은 경우로 갱신한다
'''
from itertools import permutations, combinations

INF = int(1e9)


def devide_team(ability: list):
    global N, ans
    # start, link = set(), set()

    for comb in combinations(range(N), N//2):
        start = comb
        link = set(range(N)) - set(start)
        start_sum, link_sum = 0, 0
        for (i, j) in permutations(start, 2):
            start_sum += ability[i][j]

        for (i, j) in permutations(link, 2):
            link_sum += ability[i][j]

        ans = min(ans, abs(start_sum-link_sum))


N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
ans = INF

devide_team(ability)

print(ans)
