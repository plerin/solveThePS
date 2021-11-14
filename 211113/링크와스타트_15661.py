'''
어제 다른 사람 풀이를 본 대로 풀어볼거야
1. 스타트와 링크 문제와 다른 점은 a/b 그룹을 나눌 때 두 팀의 인원수는 같지 않아도 되고 한 명 이상이여야 한다.

접근
1. n명이 주어졌다면 1~(n-1)명까지의 조합의 수를 구해야함 b그룹 = 전체 멤버 - a그룹 인원 _ combinations 라이브러리 사용
2. n명의 멤버를 모두 담을 리스트 필요 _ 전체 - a 그룹 = b그룹 ==> set 이용
3. 능력치 최소 차를 갱신 _ a그룹이 a명일 때를 총 합쳐서 모든 경우에 대한 최소 비용(ret)
'''

from itertools import combinations
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
tot_member = [i for i in range(n)]  # total member
table = [list(map(int, input().split())) for _ in range(n)]
ret = INF

for i in range(1, (n//2)+1):  # 이렇게만 구하면 모든 조합의 경우를 구할 수 있어
    div_member = combinations(tot_member, i)
    min_diff = INF

    for member in div_member:
        mem_start = list(member)
        mem_link = list(set(tot_member) - set(mem_start))  # 전체 인원 - start 그룹
        start_tot_num, link_tot_num = 0, 0

        for i in range(n-1):
            for j in range(n-1):
                try:
                    start_num = table[mem_start[i]][mem_start[j]]
                except IndexError:
                    start_num = 0
                try:
                    link_num = table[mem_link[i]][mem_link[j]]
                except IndexError:
                    link_num = 0
                start_tot_num += start_num
                link_tot_num += link_num

        diff = abs(start_tot_num-link_tot_num)
        min_diff = min(min_diff, diff)

    ret = min(ret, min_diff)

print(ret)
