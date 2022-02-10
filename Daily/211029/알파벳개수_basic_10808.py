'''
알파벳 소문자로만 이루어진 단어 S가 주어지면 각 알파벳이 단어에 몇 개 포함되어있는지
키포인트 : from a to z까지 어떻게 간결히 표현하는 방법
a = [chr(c) for c in range(ord('a'), ord('z')+1)]
'''

# table = [chr(c) for c in range(ord('a'), ord('z')+1)]
# ret = [0] * len(table)

# S = input()

# for c in S:
#     ret[table.index(c)] += 1

# print(*ret, sep=' ')


ret = [0] * 26

for i in input():
    ret[ord(i)-ord('a')] += 1

print(*ret, sep=' ')
