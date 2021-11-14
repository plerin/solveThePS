'''
> P
스타트와 링크 문제에서 그룹이 1명이상이면 됨
> S
재귀로 풀고싶은데 그보다 잘 모르겠으니 다른 사람의 식을 이해하며 풀어보자
> L
1. combination(library)로 1~(n/2)+1 까지의 조합을 구한다 _ 저 범위로만 구하면 모든 범위를 구하는 것과 같아 a/b 그룹의 비교하기 때문에
2. 모든 경우에 대해 start팀과 link팀으로 나눠(link = all member - start's member _ set() 이용)
3. n-1으로 이중 반복문(그룹은 1명 이상이니까 == 한 그룹에 n명이 될 일이 없으니까 n-1) 
4. 각 팀(start/link)의 sum을 구해 차(diff)의 최소 값을 ret의 최소값으로 갱신
> prepare
1. INF 변수 _ int(1e9)
2. 라이브러리 _ from itertools import combanation
'''
from itertools import combinations

INF = int(1e9)

n = int(input())
synerge = [list(map(int, input().split())) for _ in range(n)]
tot_member = [i for i in range(n)]  # 모든 멤버를 만들어 놔
ret = INF

for i in range(1, (n//2)+1):
    div_member = combinations(tot_member, i)
    min_diff = INF

    for member in div_member:
        start_grp = list(member)
        # 모든 멤버 중 start 그룹 멤버인 사람을 제외한 모든 사람
        link_grp = list(set(tot_member) - set(start_grp))
        # print(start_grp, link_grp)
        start_tot_sum, link_tot_sum = 0, 0

        for i in range(n-1):
            for j in range(n-1):
                try:
                    # 만약 1:3이면 1의 값은 0이다 실제로 그렇지 않지만 이 문제에선 상관 없어
                    start_tot = synerge[start_grp[i]][start_grp[j]]
                except IndexError:
                    start_tot = 0
                try:
                    link_tot = synerge[link_grp[i]][link_grp[j]]
                except IndexError:
                    link_tot = 0
                start_tot_sum += start_tot
                link_tot_sum += link_tot
        # print(start_tot_sum, link_tot_sum)
        diff = abs(start_tot_sum - link_tot_sum)
        # start / link 그룹이 i명 : tot_member - i명 으로 나눴을 때 경우의 수 중 한 번에서 최솟 값
        min_diff = min(min_diff, diff)

    ret = min(ret, min_diff)    # i : tot-i 그룹일 때의 최솟값

print(ret)
