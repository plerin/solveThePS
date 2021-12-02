'''
> P
1~n 자연수 중 길이가 M인 수열 모두 구하라
    - 같은 수 여러번 사용 가능
    - 비내림차순(앞 수보다 커야함)

keypoint
1. 앞 수와 같거나 큰 수를 구해야 한다.
    - for i in range(now,N+1)
        recursive(i, seq)
'''


def findSeq(now: int, seq: list):
    global N, M

    if len(seq) == M:
        print(*seq)
        return

    for i in range(now, N+1):
        seq.append(i)
        findSeq(i, seq)
        seq.pop()


N, M = map(int, input().split())

findSeq(1, [])
