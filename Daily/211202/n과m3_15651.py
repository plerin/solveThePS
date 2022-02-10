'''
> P
1~n 자연수가 주어졌을 때 길이 M인 모든 수열 구하라
    - 같은 수를 여러 번 골라도 된다.

n = 2 , m = 2 -> 1,1 & 1,2 & 2,1 & 2,2 모두 가능

func(findSeq)
    - param : seq(list) _ 선택한 부분 수열
    - vari : global N,M
    - logic
        1) base_condition : if len(seq) == m
        2) for i in range(1, N+1)
        3) seq.append(i); findSeq(seq); seq.pop()
'''


def findSeq(seq: list = []):
    global N, M

    if len(seq) == M:
        print(*seq)
        return

    for i in range(1, N+1):
        seq.append(i)
        findSeq(seq)
        seq.pop()


N, M = map(int, input().split())

findSeq()
