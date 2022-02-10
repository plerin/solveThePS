'''
[P]
공포도에 따라 모험가 그룹을 만들어야 하는데 만들 수 있는 그룹 수의 최댓값
    - 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 그룹에 참여
[S]
공포도 기준으로 정렬한 뒤 작은 순서대로 뽑으며 그룹 만들기
    - 정당성 : 그룹에 속하지 못하는 모험가는 남아도 되기 때문에 공포도 낮은 인원으로 먼저 그룹을 짜는게 공포도 높은 인원부터 그룹을 짜는 것보다 더 많이 만들 수 있음
[L]
함수 이용
    - PARAM : users(list)
    - LOGIC
        1. sorted(user, reverse=True) _ 내림차순 정렬 후 pop()으로 공포도 낮은 유저먼저 뽑아 s(stack)에 담아
        2. max(s)과 len(s)이 같으면 s를 비우고 cnt+=1
    - RETURN : cnt(int) 그룹 수
'''


# def makeGroup(users):
#     s = []
#     cnt = 0
#     for u in sorted(users):
#         s.append(u)
#         if max(s) == len(s):
#             s = []
#             cnt += 1
#     return cnt


def makeGroup(users):
    num = 0
    cnt = 0
    for u in sorted(users):
        num += 1
        if num >= u:  # 현재 포함된 모험가의 수가 공포도 이상이라면 그룹 만들기
            num = 0
            cnt += 1
    return cnt


N = int(input())
users = list(map(int, input().split()))

ret = makeGroup(users)

print(ret)
