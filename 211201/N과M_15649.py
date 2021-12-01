'''
> P
1~N 자연수 중 길이가 M인 모든 수열을 출력
    - 오름차순

재귀 풀이 하자!!

function(findSeq)
    - param : now:int, last:int, seq:list
    - vari : ret:list _ 기저에서 반환된 목록 여기에 append
    - logic
        1) base-condition : if len(seq) == M then return seq
        2) for i in range(now, last):
        3) seq.append(i)
        4) ret.append(findSeq(i+1,last,seq))
        5) seq.pop()
    - 

def findSeq(last:int, part:list):
    - 기저 조건 : if len(part) == M then return part
    - logic
        1) for i in range(1,last):
        2) A.append(findSeq(i,  ))

'''


# def findSeq(now: int, seq: str):
#     global M
#     ret = []

#     if len(seq) == M:
#         return seq

#     for i in range(now, N+1):
#         ret.append(findSeq(now+1, seq+str(i)))

#     return ret


def findSeq(now: int, seq: str):
    global M, ans
    # ret = []

    if len(seq.split()) == M:
        ans.append(list(map(int, seq.split())))
        # return seq
        return

    for i in range(now, N+1):
        # seq.append(str(i))
        # ret.extend(findSeq(now+1, seq))
        findSeq(now+1, seq+' '+str(i))
        # seq.pop()

    # return ret


N, M = map(int, input().split())
ans = []
findSeq(1, '')

print(sorted(ans))
