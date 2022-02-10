'''
> P
n개 자연수 중 m개를 고른 수열 모두 반환
    - 같은 수 여러 번 선택 가능
    - 비내림차순 -> 이전 값보다 현재 값이 같거나 커야한다.

> keypoint
1. 비내림차순
    -> 이전 값보다 현재 값이 같거나 커야한다.
    -> now(int)를 param으로 전달해서 이전 값을 갖지 못하도록 함


'''


def findSeq(now: int, seq: list):
    global N, M, tot_seq

    if len(seq) == M:
        print(*seq)
        return

    for idx in range(now, len(tot_seq)):
        seq.append(tot_seq[idx])
        findSeq(idx, seq)
        seq.pop()


N, M = map(int, input().split())
tot_seq = list(map(int, input().split()))

tot_seq.sort()

findSeq(0, [])
