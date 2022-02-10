'''
> P
N명 중 2그룹으로 나눴을 때 팀의 능력치의 차가 최소 인 경우 출력
    - N은 항상 짝수로 주어진다.
    - Sij와 Sji는 다를 수 있다.
> S
접근
    1) 0을 기준으로 n/2 그룹을 만들며 이 때 최소 비용(두 그룹의 능력치 차)인 경우를 갱신
    2) 그룹의 능력치 구하는 방법 ex) N=4, 13/24로 나뉘었으면 abs(s13+s31 - s24+s42) 로 구하면 된다.
    3) n명 중 n//2명의 조합을 구하고 그룹 인원이 n//2명일 때(base-condition) 최솟 값 갱신
'''

import sys

input = sys.stdin.readline


def solve(now: int, grp: list):
    global ret
    if len(grp) == N//2:
        grp_b = [i for i in range(N) if i not in grp]
        sum_a, sum_b = 0, 0

        for i in grp:
            for j in grp:
                sum_a += table[i][j]

        for i in grp_b:
            for j in grp_b:
                sum_b += table[i][j]

        ret = min(ret, abs(sum_a-sum_b))

        return

    for i in range(now, N):
        grp.append(i)
        solve(i+1, grp)
        grp.pop()

# def solve(now: int, cnt: int):
#     global ret
#     if cnt == N//2:
#         start, link = 0, 0

#         for i in range(N):
#             for j in range(N):
#                 if select[i] and select[j]:
#                     start += table[i][j]
#                 elif not select[i] and not select[j]:
#                     link += table[i][j]
#         ret = min(ret, abs(start-link))
#         return

#     for i in range(now, N):
#         if select[i] == 1:
#             continue
#         select[i] = 1
#         solve(i+1, cnt+1)
#         select[i] = 0


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
# select = [0 for _ in range(N)]
ret = sys.maxsize
solve(0, [])
print(ret)
