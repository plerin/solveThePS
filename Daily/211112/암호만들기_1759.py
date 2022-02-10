'''
> P
C개의 서로 다른 알파벳으로 L글자의 암호가 있는데 가능성 암호 모두 구하여라
    - 암호는 알파벳 소문자로 구성 
    - 최소 한개의 모음과 최소 두 개의 자운으로 구성
    - 알파벳이 정렬
> S
주어진 조건 중 가능한 모든 경우 구하라 -> 재귀로 풀어보자
접근
    - 재귀 : 큰 문제를 작은 부분 문제로 쪼개서 풀이
    - param : char(list) :문자열 담긴 리스트, arr(list) : 선택 문자가 담긴 리스트
    - bc : if len(arr) == l -> 모음수가 0이 아니고 len-모음수 >= 2일 때 출력
    - logic : 문자마다 append() -> pop()
'''


import sys


def sol(cur: int, arr: list):
    # ret = []
    if len(arr) == L:
        num_vowel = len([c for c in arr if 'aeiou'.find(c) != -1])
        if num_vowel != 0 and L - num_vowel >= 2:
            # ret.append(''.join(arr))
            print(''.join(arr))
        return

    # for c in chars:
    for i in range(cur, C):
        # if arr and (c in arr or arr[-1] > c):
        if arr and chars[i] in arr:
            continue
        arr.append(chars[i])
        sol(cur+1, arr)
        arr.pop()


# L, C = map(int, input().split())
# chars = list(map(str, input().split()))
# chars.sort()
# print(chars)
# ret = []

# sol(0, [])
# print(*sorted(ret), sep='\n')


# def solve(len, idx):
#     if len == L:
#         vo, co = 0, 0
#         for i in range(L):
#             if arr[i] in 'aeiou':
#                 vo += 1
#             else:
#                 co += 1
#         if vo > 0 and co > 1:
#             print(''.join(arr))
#         return

#     for i in range(idx, C):
#         if check[i] == False:
#             arr.append(char[i])
#             check[i] = True
#             solve(len+1, i+1)
#             check[i] = False
#             del arr[-1]


# L, C = map(int, input().split())
# check = [False] * C
# arr = []
# char = input().split()
# char.sort()
# solve(0, 0)


def solve(idx: int, ret: list = []):
    if len(ret) == L:
        vo = sum([1 for i in ret if i in 'aeiou'])

        if vo != 0 and L - vo >= 2:
            print(''.join(ret))
        return

    for i in range(idx, C):
        if char[i] in ret:
            continue

        ret.append(char[i])
        solve(i+1, ret)
        ret.pop()


L, C = map(int, input().split())
char = input().split()
char.sort()
solve(0)
