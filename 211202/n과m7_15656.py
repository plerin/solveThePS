'''
> P

> keypoint
1. 같은 수를 여러 번 골라도 된다.
    -> 1,7 & 7,1 둘 다 가능
    -> for num in tot_seq & param은 part(list)만 사용
'''


def findSeq(part: list):
    global N, M, tot_seq

    if len(part) == M:
        print(*part)
        return

    for num in tot_seq:
        part.append(num)
        findSeq(part)
        part.pop()


N, M = map(int, input().split())
tot_seq = sorted(list(map(int, input().split())))

findSeq([])
