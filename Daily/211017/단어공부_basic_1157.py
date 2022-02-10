'''
problem
1. 가장 많이 사용된 알파멧 반환
keypoint
1. 가장 많이 사용된 알파벳 존재 중복 여부 체크
'''
# from collections import Counter

# counter = Counter(input().upper())

# ret, pre = '', 0

# for c, n in counter.most_common(2):
#     if pre == 0:
#         ret, pre = c, n
#     elif pre == n:
#         ret = '?'

# print(ret)


x = input().upper()
l = [x.count(c) for c in set(x)]
print(max(set(x), key=x.count) if l.count(max(l)) == 1 else '?')
