'''

keypoint
    1. 중복되는 수열은 여러 번 출력 x
        -> 재귀 호출 now+1 를 주고 range(now)부터 시작
        -> param에 now(int) 추가
'''


def findSeq(now: int, part: list):
    global N, M, seq

    if len(part) == M:
        print(*part)
        return

    for i in range(now, len(seq)):
        part.append(seq[i])
        findSeq(i+1, part)
        part.pop()


N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))

findSeq(0, [])
