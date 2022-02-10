'''
영어 알파벳(대문자/소문자)를 13글자씩 밀어서 만든다
대문자인 경우 +13 값이 ord('Z')를 넘으면 -13
소문자인 경우 +13 값이 ord('z')를 넘으면 =13
'''
# S = input()
# ret = ''
# for c in S:
#     if c.isalpha():
#         if c.islower():
#             if ord(c)+13 > ord('z'):
#                 c = chr(ord(c)-13)
#             else:
#                 c = chr(ord(c)+13)
#         else:
#             if ord(c)+13 > ord('Z'):
#                 c = chr(ord(c)-13)
#             else:
#                 c = chr(ord(c)+13)
#     ret += c

# print(ret)


def f(c):
    i = ord(c)
    if i > 96:  # 대문자 알파벳이라면
        # 'A' 값(97)에서 알파벳 수의 절반(13)을 뺀 값인 84를 i에서 뺌으로써 잘반을 나누고 다시 97로 더해준다.. 진짜 천재다
        return chr((i-84) % 26+97)
    if i > 64:  # 소문자 알파벳이란
        return chr((i-52) % 26+65)
    return c  # 숫자 또는 띄어스기라면


print(''.join(map(f, input())))
