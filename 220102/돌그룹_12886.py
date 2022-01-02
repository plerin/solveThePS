'''
>> P
돌을 세 그룹으로 만들고 각 개수는 A,B,C개라고 했을 때 돌을 움직여 세 그룹의 돌을 같은 개수로 만들수 있는가?
    - 두 그룹을 고르고 작은 쪽은 X, 큰 쪽을 Y라고 정하고
    - X = X*2 , Y = Y-X로 만들기를 반복한다
>> S
BFS라고 안 느껴짐..
>> 전략
1. 3개 그룹이 있고 개수가 서로 다른 2개 그룹 선택해서 연산 수행
    - 서로 같은 개수가 없으면 2번 // 있으면 1번 // 모두가 같으면 종료
    - BFS로 해당 상황에서 모든 경우를 QUEUE에 넣어 반복 수행
        -> A와 B, A와 C 그리고 B와 C를 모든 경우에서 추가
        -> 시작을 무엇부터 하느냐에 따라 그 이후 연산이 모두 달라지니까 시작을 3개로 출발
        (A, B), (A, C), (B, C)
2. 만들 수 없는 경우는 어떤 상황일 까?
    - A,B에서 30, 30이 나왔는데 또다시 A,B에서 30, 30이 나오면 그건 제외
    단, B,C에서 30, 30이 나오면 그건 또 다른 문제 연산이 다르기 때문에
    -> 각 연산에 대한 값의 중복(VISITED)을 확인
        -> MAX값이 없으니까 SET에 담아놓을까?
            (A, B, AV, BV) # (A그룹, B그룹, A값, B값)

'''

# from collections import deque


# def solve():

#     visited = set() # 방문 처리하기 위함
#     comb = [('A', 'B'), ('A', 'C'), ('B', 'C')] # 3가지 연산을 반복해야 함
#     queue = deque(comb)

#     while queue:
#         g1, g2 = queue.popleft()
#         is_equal = cal(g1, g2)  # 2개 그룹을 선택해 연산 수행
#         if not is_equal and (g1, g2, group[g1], group[g2]) not in visited:
#             visited.add((g1, g2, group[g1], group[g2]))
#             queue.append((g1, g2))


# def cal(x: str, y: str):
#     global group
#     is_equal = False

#     if group[x] > group[y]:
#         group[x] -= group[y]
#         group[y] += group[y]
#     elif group[y] > group[x]:
#         group[y] -= group[x]
#         group[x] += group[x]
#     else:
#         is_equal = True
#     return is_equal

# # 입력값을 dict {알파벳:숫자} 형태로 받았다
# group = {chr(idx+65): int(val) for idx, val in enumerate(input().split())}

# solve()

# print(1 if len(set(group.values())) == 1 else 0)    # 알파벳에 매칭되는 숫자가 모두 같으면 1 다르면 0


# 풀이 2 dict 사용
'''
풀이 2. 
>> 아이디어
1. defaultdict 활용 중복 처리
    - visited = defaultdict(bool) & visited[tupe(stones)] = True
2. 3개 그룹의 합은 항상 동일하다
    - x + x 와 y - x해도 총량은 동일
    -> tot = sum(stones) & z = tot-x-y
'''




from collections import deque, defaultdict
def solve():
    global visited

    queue = deque([stones])
    visited[tuple(stones)] = True

    while queue:
        a, b, c = queue.popleft()

        if a == b == c:
            return 1
        for x, y in ((a, b), (b, c), (a, c)):
            a, b, c = cal(x, y)

            if not visited[(a, b, c)]:
                visited[(a, b, c)] = True
                queue.append((a, b, c))

    return 0


def cal(x: int, y: int):
    if x == y:
        return x, y, tot-x-y
    elif x > y:
        return x-y, y+y, tot-x-y
    elif y > x:
        return x+x, y-x, tot-x-y


stones = list(map(int, input().split()))
visited = defaultdict(bool)
tot = sum(stones)

ans = solve()
print(ans)
