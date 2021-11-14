'''
문자열(S)가 주어졌을 때 단어만 뒤집으려고 한다
    - 태그는 단어가 아니고 태그와 단어 사이에 공백이 없다
    - 단어는 공백으로 구분
접근
    - 2번에 나눠 자르면 어때? 1차 (<) // 2차 (>) 이럴 때 [0]은 앞뒤로 [] 붙여서 정방 // [1]은 역방[::-1]
    s.split("<")
'''

# s = input()

# items = list(map(str, s.split("<")))

# if items[0] != '':
#     print(' '.join(list(map(lambda x: x[::-1], items[0].split()))), end='')

# for item in items[1:]:
#     for i, val in enumerate(item.split(">")):
#         if i == 0:
#             print(f'<{val}>', end='')
#         else:
#             print(
#                 *list(map(lambda x: x[::-1], val.split())), sep=' ', end='')

'''
접근
1. 입력 문자열을 리스트로 받는다.
2. while로 index가 문자열 끝까지 갈 때동안 반복문 
3. '<' / 알파벳 / 띄어쓰기 일때를 구분하여 처리
    - '<' 만나면 '>'를 가르킬 때까지 idx+=1
    - 알파벳 만나면 start 정하고 알파벳 끝날 때까지 idx+=1 그리고 word[start:idx] = reverse로 갱신
    - if 띄어쓰기 then 인덱스 증가
'''


import sys
input = sys.stdin.readline

word = list(input().rstrip())
ret = []
idx = 0

while idx < len(word):
    if word[idx] == "<":
        start = idx
        while word[idx] != ">":
            idx += 1
        idx += 1
        ret.append(''.join(word[start:idx]))
    elif word[idx].isalnum():
        start = idx
        while idx < len(word) and word[idx].isalnum():
            idx += 1
        tmp = word[start:idx]
        tmp.reverse()
        word[start:idx] = tmp
        ret.append(''.join(word[start:idx])[::-1])
    else:
        ret.append(word[idx])
        idx += 1

print(''.join(word))
print(''.join(ret))
