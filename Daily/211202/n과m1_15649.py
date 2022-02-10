'''
> P
1~n까지 수열 중 길이가 m개인 수열 모두 구하시오
    - 중복 없음
    - 오름차순 출력

반복

재귀
1,2,3 // 1,3,2 가 나올 수 있어야 한다
    -> 1~n까지 반복하는데 이미 뽑은 수열의 값은 제외 
    -> if n in sel then continue else call recursive(sel:list)
'''


# def findSeq(seq: list):
#     global N, M

#     if len(seq) == M:
#         print(*seq)

#     for i in range(1, N+1):
#         if i in seq:
#             continue
#         seq.append(i)
#         findSeq(seq)
#         seq.pop()

def findSeq(seq: list):
    global N, M
    ret = []

    if len(seq) == M:
        # print(*seq)
        return ' '.join(map(str, seq[::]))

    for i in range(1, N+1):
        if i in seq:
            continue
        seq.append(i)
        ret.append(findSeq(seq))
        seq.pop()

    return ret


N, M = map(int, input().split())

ans = findSeq([])

print(*ans)
