'''
> P
n명이 있고 n/2명으로 짝지어 스타트 / 링크 팀을 이룬다 이 때 양 팀의 능력치 차가 최소인 경우
    - 두 팀이 인원이 같지 않아도 되지만 한 명이상이여야 함
    - 팀의 능력치(abillity) = 모든 쌍의 능력치 Sij의 합
        ex) 1,2,3 팀이면 S12 + S21 + S13 + S31 + S23 + S32 (N개 중 N개 순열?!)
        -> list(permutation(range(1,4),2))

> S
1. 팀을 나눈다 (1~N//2) _ 6명이면 1,2,3 명 구하면 나머지 경우 다 구하기 때문
for num in range(1,N//2+1):
    for comb in combination(range(N),num)
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
        1) 팀을 나눈다 (start / link) _ 1팀이 1명~N//2명인 경우까지 반복하며
        2) 팀별 합을 구한다
        3) 가장 작은 경우로 갱신한다
'''
from itertools import permutations, combinations

INF = int(1e9)


def devide_team(ability: list):
    global N, ans

    for num in range(1, N//2+1):
        for comb in combinations(range(N), num):
            # 비트마스크 써보는거 어떨까?
            '''
            1. start,link = [0]
            2. range(N) 반복하며 if comb 있으면 start | 1<<i else link | 1<<i
            3. if start & 1<<i and start 1<<j then ,
            '''
            start, link = 0, 0
            for i in range(N):
                if i in comb:
                    start = start | 1 << i
                else:
                    link = link | 1 << i

            start_sum, link_sum = 0, 0

            for i in range(N):
                for j in range(N):
                    if i == j:
                        continue
                    if start & 1 << i and start & 1 << j:
                        start_sum += ability[i][j]
                    elif link & 1 << i and link & 1 << j:
                        link_sum += ability[i][j]

            ans = min(ans, abs(start_sum-link_sum))

            if ans == 0:
                return


N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
ans = INF

devide_team(ability)

print(ans)
