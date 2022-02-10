'''
>> P
한 행이 2**n인 정사각 배열을 z모양으로 탐색하려고 한다.
N > 1 인 경우 2**(n-1)으로 4등분 한후 재귀적 순서대로 방문한다
>> S
4등분 되는 사각형 
n = 1, 4개
n = 2, 16개(4 * 4)
n = 3, 64개(16 * 4)
n = 4, 16*16 = 256개(64 * 4)
...

접근
n == 1 인 경우와 n > 1인 경우로 나눠 풀이
if n == 1:
    x * 2 + y * 1 , ex) r=1,c=0 -> 2 + 0 = 2
else:
    #n == 3 이라면.. (0,0), (0,4),(4,0),(4,4)
    for i in range(2):
        for j in range(2):
            (2**(n-1)*i, 2**(n-1)*j, n-1)

    size = 2**(n-1) * 2**(n-1) 을 더해줘 값에 
    cnt = 0
    for i in range(row, row+size):
        for j in range(col, col+size):
            if i == r and if j == c:
                return cnt+size
    return False

재귀를 반복한다
N이 1이될 때까지 그리고 1이되면 규칙대로 증가시킨다 만약 그 중 (r,c)를 만나면 종료

1. N이 1이 될 때까지 재귀 호출(사각형을 4등분으로 자른다)
2. N ==1 일 때 cnt로 계속 증가시킨다
3. 그 중 (r,c)를 만나면 종료?
'''


def solve(row: int, col: int, size: int):
    global cnt
    flag = False
    # size == 1일 때
    if size == 1:
        if row <= r <= row+1 and col <= c <= col+1:
            print((r-row)*2 + (c-col) + cnt)
            flag = True
            # exit(0)
        cnt += 4
        return flag
    # 아닐 때

    for i in range(2):
        for j in range(2):
            flag = solve(row+2**(size-1)*i, col+2**(size-1)*j, size-1)
            if flag:
                return flag
            # (0, 0, 2), (0, 4, 2), (4, 0, 2), (4, 4, 2)
            # (0, 0, 1), (0, 2, 1), (2, 0, 1), (2, 2, 1)
            # (0, 4, 1), (0 ,6, 1)..
    return flag


N, r, c = map(int, input().split())
cnt = 0
solve(0, 0, N)
