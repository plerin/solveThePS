'''
kp
#1. 문자와 숫자와 매칭시킨다.
#2. 숫자당 소요 시간 = 숫자+1
'''


# dial = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5, 'M': 6,
#         'N': 6, 'O': 6, 'P': 7, 'Q': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9, 'Z': 9}

# # 입력받기
# ret = 0
# for c in input():
#     ret += dial[c]+1

# print(ret)


dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

ret = 0
for c in input():
    for i in dial:
        if c in i:
            ret += dial.index(i) + 3

print(ret)
