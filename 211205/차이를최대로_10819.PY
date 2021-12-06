'''
> P
N개 정수로 이루어진 배열 a가 있을 때 순서를 바꿔 최대 값을 만드는 프로그램
    - | ai-2 - ai-1 | 이 가장 큰 값이 나오려면 
        1. 부호가 다르거나
        2. 두 값의 차이가 커야한다. (== 부호가 다르다면 차이가 크다)
'''

from itertools import permutations

# 라이브러리 활용(permutations)


def usingLibrary(seq: list):
    global N
    ret = 0
    for perm in permutations(seq, N):
        ret = max(ret, sum([abs(perm[i] - perm[i+1])
                            for i in range(N-1)]))

    return ret

# 다음 순열 알고리즘 활용


def nextPermutation(seq: list):
    global N
    x, y = 0, 0

    seq = sorted(seq)
    desc_seq = sorted(seq, reverse=True)
    ret = sum([abs(seq[i] - seq[i+1])
               for i in range(N-1)])

    while seq != desc_seq:
        for i in range(N-1, 0, -1):
            swap = False
            if seq[i-1] < seq[i]:
                x, y = i-1, i

                for j in range(N-1, 0, -1):
                    if seq[j] > seq[x]:
                        seq[x], seq[j] = seq[j], seq[x]
                        swap = True
                        break
            if swap == True:
                seq = seq[:y] + sorted(seq[y:])
                ret = max(ret, sum([abs(seq[i] - seq[i+1])
                                    for i in range(N-1)]))
                break

    return ret


N = int(input())
arr = list(map(int, input().split()))

ans1 = usingLibrary(arr)
# ans2 = nextPermutation(arr)

print(ans1)
# for comb in permutations(arr, len(arr)):
#     ans = max(ans, sum([abs(comb[i] - comb[i+1])
#                         for i in range(len(comb)-1)]))


# print(ans)
