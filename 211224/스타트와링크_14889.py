'''
>> P
1~N을 번호로 갖는 N명이 2팀으로 나뉘어서 축구를 하려고 할 때 능력치의 합이 최소인 경우 구하라
    - N은 짝수이고 팀은 N/2로 나눈다
    - Sij = i번 사람과 j번 사람이 같은 팀 속했을 때 능력치, Sij와 Sji는 다를 수 있다
>> S
1. N명(1~N)을 2팀으로 나눈다
    -> start = case , link = range(1,N) - start
2. 팀별로 조합(permutations)을 구하고 그를 통해 시너지 합을 더해준다
3. 2번 각 팀의 능력치 합의 차를 구해서 최소 값을 갱신

>> F
def make_team(person: int):
    - vari : global abil(list), ans
    - logic
        1) 팀을 나눈다 _ permutations(range(1,person), person/2)
        2) 각 팀의 조합으로 능력치의 합을 구한다
        3) 팀의 능력치 차이로 ans을 갱신한다
'''

from itertools import permutations, combinations


def make_team(person: int):
    global ans

    for case in combinations(range(N), N//2):
        # start = list(case)
        # link = [p for p in range(N) if p not in start]
        start = case
        link = set(range(N)) - set(start)
        start_sum, link_sum = 0, 0

        for a, b in permutations(start, 2):
            start_sum += abil[a][b]
        for a, b in permutations(link, 2):
            link_sum += abil[a][b]

        if abs(start_sum - link_sum) < ans:
            ans = abs(start_sum - link_sum)


N = int(input())
abil = [list(map(int, input().split())) for _ in range(N)]

ans = 1e9

make_team(N)

print(ans)
