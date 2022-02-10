'''
> P
1~49 숫자 중 6개를 고르는데 오름차순 순열을 구하라(i-1 수가 i수보다 작아야 해)
    - 오름차순으로 주어진다.
    - 마지막 줄에 0이 주어진다.
    - 테스트 케이스 간 빈 줄 하나 출력

> S
1. 라이브러리(combinations) 활용
모든 조합 구하고 그 중 오른차순 정렬된 값만 표출
def usingLibrary(arr:list)
    global N
    for comb in combinations(arr, 6):
        if comb == sorted(comb) then print

2. dfs 백트래킹 활용
이미 오름차순된 입력 배열을 길이가 6인 순열을 뽑는다.
n과 m 알고리즘_순열 알고리즘 사용
def permutationLogic(start:int, visit:list)
    if len(visit) == 6:
        print()
        return

    for i in range(start, N):
        if i in visit:
            continue
        visit.append()
        pumutaionloginc(i,visit)
        visit.pop()
'''
from itertools import combinations


def usingLibrary(arr: list):
    for comb in combinations(arr, 6):
        print(*comb)


def usingLogic(start: int, visit: list):
    global k
    if len(visit) == 6:
        print(*visit)
        return

    for i in range(start, k):  # start부터 시작하니까 start 뒤 숫자가 6개가 안되면 안 돌아!
        if arr[i] in visit:
            continue
        visit.append(arr[i])
        usingLogic(i, visit)
        visit.pop()
    pass


while True:
    k, *arr = map(int, input().split())

    if k == 0:
        break

    # usingLibrary(arr)
    usingLogic(0, [])
    print()
#
