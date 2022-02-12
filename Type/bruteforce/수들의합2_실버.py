'''
backjoon url -> https://www.acmicpc.net/problem/2003

>> Keyword


>> P
N개의 수로 된 수열이 있을 때 i부터 j번째 수의 합이 M이 되는 경우의 수를 구하라
    - 수가 붙어있어야 함(연속적)
>> S
완전탐색으로 구현하여 start 0부터 나아가며 누적 값이 M보다 크거나 같을 경우를 종료조건
    - M과 같으면 True -> global ans + 1 & return
    - M보다 크면 return

코딩
1. 방문처리할 리스트 생성
visited = [False] * N
2. 메소드 선언
def get_case(start, accum) -> None
    if accum >= M:
        if accum == M: ans += 1
        return
    
    for i in range(start, N):
        if not visited[arr[i]]:
            visited[arr[i]] = True
            get_case(start, accum+arr[i])
            visited[arr[i]] = False

'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def get_case(start: int, depth: int, accum: int) -> None:
    global ans
    # 종료조건 = 누적 합이 M보다 크거나 같으면
    if accum >= M:
        if accum == M:
            ans += 1
        return True

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            # 종료조건을 만날 때까지 재귀 & 누적합이 M or M보다 크던 상관없이 최소 start에서 탐색을 끝나야해
            if get_case(i, depth+1, accum+arr[i]):
                visited[i] = False
                if depth != 0:
                    break
                    return True
    return True


N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * N
ans = 0

get_case(0, 0, 0)

print(ans)


# 마지막 지점을 기억하며 앞인덱스 값을 빼가며 진행
def numberOfCase(n, m):
    global data
    end = 0
    interval_sum = 0
    cnt = 0

    for start in range(n):
        #  start부터 m보다 작으면 반복
        while interval_sum < m and end < n:
            interval_sum += data[end]
            end += 1

        if interval_sum == m:
            cnt += 1
        # 마지막에 시작 인덱스 빼기(1번째 빼고 2번째 인덱스부터 시작하기 위해)
        interval_sum -= data[start]

    return cnt


def num(n, m):
    global data
    end = 0
    interval_sum = 0
    cnt = 0

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += data[end]
            end += 1

        if interval_sum == m:
            cnt += 1

        interval_sum -= data[start]

    return cnt


n, m = map(int, input().split())
data = list(map(int, input().split()))

ret = numberOfCase(n, m)

print(ret)
