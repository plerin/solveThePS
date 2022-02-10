'''
[P]
집에 콘센트 꽃을 수 있는 플러그가 1개 있고 멀티탭이 많을 때 최대 몇 대의 컴퓨터의 전원에 연결 할 수 있나?

[L]
N : 멀티탬 수
1. 수식 = SUM(멀티탭 플러그 수) - (N-1)  # 멀티탭과 멀티탭을 이어주는 플러그를 1개씩 빼야함(맨 마지막 멀티탭 제외)
'''

import sys

input = sys.stdin.readline

N = int(input())

plugs = [int(input())-1 for i in range(N)]

print(sum(plugs)+1)
