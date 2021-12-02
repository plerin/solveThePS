'''
> P
1~n까지 자연수 중 중복 없이 M개 고른 수열
    - 오름차순 출력

keypoint
1. 중복 없다 -> 1,2 와 2,1 은 같은 값 -> 1,2만 출력(오름차순)

풀이
1. from itertools import combinations 사용
2. 재귀

function(findSeq)
    - param : now(int), seq(str) _ 부분 수열 값을 담아 놓음
    - vari : global N, M _ 입력 값을 global로 선언하여 사용, ret(list)
    - logic
        1) base_condition : if len(seq) == M then return seq
        2) for i in range(now, N+1)
        3) ret.append(findSeq(now+1,seq+str(i)))
        4) return ret
'''

# from itertools import combinations

# N, M = map(int, input().split())

# for comb in combinations(range(1, N+1), M):
#     print(' '.join(map(str, comb)))


def findSeq(now: int, seq: str):
    global N, M
    # ret = []

    if len(seq) == M:
        print(' '.join(map(str, seq)))
        # return ' '.join(map(str, seq))

    for i in range(now, N+1):
        # ret.append(findSeq(i+1, seq+str(i)))
        findSeq(i+1, seq+str(i))

    # return ret[::]


N, M = map(int, input().split())

findSeq(1, '')

# print(*ans, sep='\n')
