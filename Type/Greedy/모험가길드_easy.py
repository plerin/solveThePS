'''
youtube url -> https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2&t=758s

>> Keyword

>> P
N명이 있고 공포도가 존재한다
공포도가 x인 모험가는 반드시 x명 이상 구성한 그룹에 참여해야 함
N명의 모험가가 있을 때 여행 떠날 수 있는 그룹 최댓값을 구하라

>> S
오름차순정렬을 해서 그룹을 지으면 가장 효율적일 것 같아
공포도가 낮은 값부터 그룹을 짓는게 가장 효율적이지 않을까?

정당성 분석
공포도나 낮은 순서부터 그룹을 맺으면 사람이 남더라도 최대한 그룹을 맺을 수 있어
중간에 공포도 높은 사람을 먼저 맺으면 같이 묶인 사람의 공포도나 낮아서 낭비될 수 있어

코드
1. 공포도 정렬 & 순서 저장(idx =0)
2. 공포도 탐색하며 idx(현재 공포도==그룹필요인원), ret(+=1) 갱신
idx = ret = 0
while idx < N:
    idx += fear[idx]
    ret += 1

'''


def make_group(num: int) -> int:
    global fear
    # idx 인원 지정 순서, ret = 그룹 수
    idx = ret = 0
    # 인덱스를 조정하며 그룹 만들 수 있는 여부 확인 (가능 -> ret +=1 불가능 -> 반복문 나와(break))
    while True:
        idx += fear[idx]

        if idx >= num:
            break
        ret += 1

    return ret


def solve2(num: int) -> int:
    global fear
    count = ret = 0

    for i in fear:
        count += 1
        if count >= i:
            ret += 1
            count = 0

    return ret


N = int(input())
fear = list(map(int, input().split()))

print(make_group(N))
