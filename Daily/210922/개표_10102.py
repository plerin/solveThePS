from collections import Counter


def counting(vote):
    cnt = Counter(vote)

    return cnt.most_common(1)[0][0] if cnt['A'] != cnt['B'] else 'Tie'


N = int(input())

VOTE = input()

ret = counting(VOTE)
print(ret)
