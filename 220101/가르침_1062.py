'''
>> P
N개 단어가 있고 K개 글자를 배워서 읽을 수 있는 단어 최댓 값을 구하기
    - 단어는 anta 로 시작하고 tica로 끝난다
    - 단어는 영어 소문자로만 구성
    - 단어 중복 없음
>> S
완전 탐색, 

전략
1. antatica의 antic는 무조건 배워야하니까(모든 단어 포함) K개에서 5개 뺀 나머지 글자 배우기
    - set(input()) - core(antic)으로 입력 받기
2. 모든 단어에서 antic를 제외한 단어만 모아서 경우의 수를 따져(combinations)
    - combinations(use_alpha, K-5) 
3. 2번에서 추린 글자들과 입력으로 주어진 단어의 글자와 매칭하여 경우 따지기
    - case의 비트마스크 합 & word_sum(비트마스크) = word_sum 이면 cnt + 1
'''

from itertools import combinations


def solve():
    global ans

    if K < 5:
        return
    comb = [2**i for i in range(26) if chr(i+97) != 'antic']
    core = sum([2**(alpha[c]) for c in 'antic'])
    for case in combinations(comb, K-5):
        cnt, bit = 0, core

        for i in case:
            bit += i

        for w in word:
            if bit & w == w:
                cnt += 1

        ans = max(cnt, ans)


N, K = map(int, input().split())
word = []
alpha = {chr(val+97): idx for idx, val in enumerate(range(26))}
for w in range(N):
    ws = 0
    for c in input():
        ws |= (1 << alpha[c])
    word.append(ws)

ans = 0

solve()

print(ans)
