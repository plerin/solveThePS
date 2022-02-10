'''
> P
1~N까지 이루어진 순열을 사전순으로 출력하시오

1. itertools 에서 permutations 사용 

2. 다음 순열 코드 그대로 사용 
    - 입력 순열 1~n까지 sort()한 리스트
    - 모든 경우 출력

'''


def totPermutation(N: int):
    seq = [i for i in range(1, N+1)]

    # for i in range(N-1, 0, -1):
    #     if seq[i-1] < seq[i]:
    #         x, y = i-1, i

    #         for j in range(N-1, 0, -1):
    #             if seq[j] > seq[x]:
    #                 seq[x], seq[j] = seq[j], seq[x]
    #                 seq = seq[:y] + sorted(seq[y:])
    #                 print(seq)

    for _ in range(24):
        for i in range(N-1, 0, -1):
            # x, y = 0, 0
            if seq[i-1] < seq[i]:
                x, y = i-1, i

                for j in range(N-1, 0, -1):
                    # print(seq[x], seq[x])
                    if seq[j] > seq[x]:
                        seq[x], seq[j] = seq[j], seq[x]
                        # print(seq)
                        break
            # break
            seq = seq[:y] + sorted(seq[y:])
            print(seq)


N = int(input())

totPermutation(N)
