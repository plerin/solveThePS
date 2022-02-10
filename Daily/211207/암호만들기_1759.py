'''
> P
서로 다른 알파벳 C개 중 최소 한개의 모음을 갖는 L개의 조합으로 이루어지는 모든 경우 출력
    - 암호는 장렬됨

> S
0. COMMON
COUNT OF 모음 : 1~(L-2)개
정렬된 값이어야 함

1. 라이브러리 활용
    - C개중 l개의 조합 중 모음이 1~(L-2) 개 있고 정렬된 경우 출력

2. 오름차순 순열 구하는 식 활용
    - 입력 값(문자들) 정렬한 데이터로 오름차순 순열을 구해
    - 기저 함수 : if len() == L then if sum([1 for c in seq if c in 'aeiou'])
'''
from itertools import combinations


def makePassword(seq: list):
    for comb in combinations(seq, L):
        vowel_cnt = sum([1 for c in comb if c in 'aeiou'])
        if 1 <= vowel_cnt and vowel_cnt <= L-2:
            print(''.join(comb))


def makePassword2(start: int, passwd: str):
    if len(passwd) == L:
        vowel_cnt = sum([1 for c in passwd if c in 'aeiou'])
        if 1 <= vowel_cnt and vowel_cnt <= L-2:
            print(passwd)
        return

    for i in range(start, C):
        if letters[i] in passwd:
            continue
        makePassword2(i, passwd+letters[i])


L, C = map(int, input().split())
letters = list(map(str, input().split()))

letters.sort()

# makePassword(letters)
makePassword2(0, '')
