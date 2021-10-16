'''
problem
1. 가장 많이 사용된 알파멧 반환
keypoint
1. 가장 많이 사용된 알파벳 존재 중복 여부 체크
'''
from collections import Counter

counter = Counter(input())

# word = list(map(str, input().upper()))
ret, pre = '', ''

for c, n in counter.most_common(2):


for c in set(word):
    num = ''.join(word).find(c)
    if ret[-1][1] == num:
        ret.append((c, num))
    elif ret[-1][1] < num:
        ret = [(c, num)]

print(ret)
if len(ret) > 1:
    print('?')
else:
    print(ret[0][0])
