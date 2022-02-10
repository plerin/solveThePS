'''
> P
1~49 수 중 6개를 특정 전략으로 뽑는 모든 경우 출력

> KP
1. 모든 순열 값 중 [i-1] 값이 [i] 값보다 작지 않은 경우 출력
    - combination 값 중 if comb != sorted(comb) continue

> solve
1. 라이브러리 사용 _ combinations
2. dfs 풀이
vari
    - comb(list) : 크기는 n 기본 값은 0
function
    - param : start(int) _ 현재 숫자(인덱스), depth(int) _ 깊이
    - vari : global seq, comb
    - logic
        1) bc : depth == n then print(comb)
        2) for i in range(start, len(seq)) -> comb[i] = seq[i]
        3) call recursive
        4) comb[i] = 0

local에서 seq로 배열 입력 받고 재귀 함수에서 global로 seq 사용함

'''


def dfs(start: int, depth: int):
    global visit

    if depth == 6:
        print(*visit)
        return

    for i in range(start, n):
        visit.append(seq[i])
        dfs(i+1, depth+1)
        visit.pop()


while True:
    n, *seq = map(int, input().split())

    if n == 0:
        break

    visit = []
    dfs(0, 0)

    print()

# from itertools import combinations


# def findAllWay():
#     global n, arr

#     for comb in combinations(arr, 6):
#         if list(comb) != sorted(comb):
#             continue
#         print(*comb)


# while True:
#     n, *arr = map(int, input().split())

#     if n == 0:
#         break

#     findAllWay()
#     print()
