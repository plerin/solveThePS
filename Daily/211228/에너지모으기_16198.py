'''
>> P
N개의 구슬이 모여있고 무게는 Wi라고 할 때 모을 수 있는 에너지 최대 값을 구하라
    - i번째 구슬의 무게는 Wi
    - x를 고르면 Wx-1과 Wx+1을 곱한 수를 얻는다
    - 첫번째 마지막번째 고를 수 없어
>> S
1. N개라면 N-2만큼 연산을 수행 (인덱스는 1~N-2를 활용) or 맨 앞에 []를 붙여 1~N 중 2~N-1을 활용
2. x번째 구슬을 제거 
    -> visited보다 remove 하고 add 하는 편이 좋겠다 
    -> 기저조건은 depth:int 가 2가 되면 ans 갱신
'''
from collections import deque
from itertools import permutations


# def use_library():
#     global weight, ans

#     for case in permutations(range(1, N-1), N-2):

#         print(case)
#         cnt = 0
#         for i in case:
#             tmp = i-cnt


def dfs(depth: int, total: int):
    global weight, ans

    if depth == 2:  # 맨 앞 / 맨 뒤만 남았을 경우
        ans = max(ans, total)
        return

    for i in range(1, len(weight)-1):
        add = weight[i-1] * weight[i+1]
        tmp = (i, weight[i])    # remove하기 전 (idx, val) 임시 저장
        # weight.remove(weight[i])  # weight에서 weight[i] 값 제거
        del weight[i]  # weight의 i번째 인덱스 제거
        dfs(depth-1, total+add)
        weight.insert(tmp[0], tmp[1])

    return


N = int(input())
weight = list(map(int, input().split()))
ans = -1e9

dfs(N, 0)
print(ans)
