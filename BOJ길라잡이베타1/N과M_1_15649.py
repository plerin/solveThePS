

def check(x):
    if x == m:
        print(*arr)
        return

    for i in range(n):
        if visit[i] == False:
            visit[i] = True
            arr[x] = i+1
            check(x+1)
            arr[x] = 0
            visit[i] = False


# n = 수열 수(1~n) // m = 선택 수
n, m = map(int, input().split())

visit = [False] * n
arr = [0] * m

check(0)
