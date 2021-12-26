'''
>> P
배열의 개수와 구성 값이 주어질 때 수를 고르는 모든 방법을 구하는 프로그램 작성
    - 여러 테스크 케이스가 있어 마지막 입력은 0
    - 결과는 사전 순으로 출력
>> S
N개의 집합에서 모든 경우 수를 구하는건
    - combinations 사용하는 방법
    - 재귀 호출하는 방법(dfs)

>> F
def use_library(num: int):
    - vari : global arr(list)
    - logic
        1) combinations 으로 num 집합을 구하고 _ arr이 오름차순이라 그대로 사용
        2) 그대로 출력
def dfs(depth: int, prev: int):
    - vari : global visited(list) _ False -> True _ 여기서 visited 는 1~49
    - logic
        1) if depth == 6 -> print(viisted if true) & return
        2) for i in range(len(arr))
            if not visited[i] and prev < i -> visited[i] = True & dfs(depth+1, i) & visited[i] = False
'''

from itertools import combinations


def use_library(num: int):
    global arr

    for case in combinations(arr, 6):
        print(*case)

    print()  # 테스트 케이스 사이 빈 줄 출력


def dfs(depth: int, prev: int):
    global visited

    if depth == 6:
        print(*[v for v in visited if v != False])
        return

    for i in range(k):
        if not visited[i] and prev < arr[i]:
            visited[i] = arr[i]  # 방문하면 해당 인덱스에 값 갱신(False -> 해당 값)
            dfs(depth+1, arr[i])
            visited[i] = False


while True:
    k, *arr = list(map(int, input().split()))

    if k == 0:
        break

    visited = [False] * k  # 입력 값(arr)를 False로 초기화

    use_library(k)
    # dfs(0, 0)
    # print()
