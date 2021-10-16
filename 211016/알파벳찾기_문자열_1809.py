'''
koypoint : 문자열 리스트 간결하게 만들기
'''

S = input()

ret = []
alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

for c in alphabet:
    ret.append(S.find(c))

print(*ret, sep=' ')
