'''
> P 
n개 자연수 중 길이가 m인 수열 모두 구하라
    - n은 모두 다른 자연수
    - 중복 수열 여러 번 출력 x 
    - 오름차순 출력

keypoint
    1. 오름차순 출력
        -> n개 자연수를 sort()하여 사용
    2. 순서 상관 없어 
        -> now없이 1부터 시작하며 seq에 없는 경우만 처리
'''


def findSeq(tot: list, part: list):
    global N, M

    if len(part) == M:
        print(*part)
        return

    for num in tot:
        if num in part:
            continue
        part.append(num)
        findSeq(tot, part)
        part.pop()


N, M = map(int, input().split())
seq = sorted(list(map(int, input().split())))

findSeq(seq, [])
