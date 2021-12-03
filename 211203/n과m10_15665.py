'''
사고를 넓게 해보자
1. combination으로 가능하지 않을까? range를 역순으로 넣어서
2.  now를 param으로 진행 단 hash(dic)으로 중복 체크 해야함
'''


def findSeq(seq: str):
    global tot_seq, collect

    if len(seq.split()) == M:
        # conv_seq = ''.join(map(str, seq))
        if seq not in collect:
            collect[seq] = 1
            print(seq)
        return

    for num in tot_seq:
        # seq.append(tot_seq[idx])
        findSeq(seq + str(num) + ' ')
        # seq.pop()


N, M = map(int, input().split())
tot_seq = list(map(int, input().split()))
collect = {}

tot_seq.sort()

findSeq('')
