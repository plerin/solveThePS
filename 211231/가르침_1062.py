'''
>> P
N개 단어가 주어지고 K개 영어단어를 통해 읽을 수 있는 단어 최대 개수 구하기
    - 모든 단어는 anta -> xx -> tica 로 구성
    - 단어는 영어 소문자로 구성, 단어 별 중복 없다.
>> S
모든 단어에 'antatica'가 들어가기 때문에 무조건 여기있는 알파벳은 알아야해
    - K 개 중 'antic'는 무조건이니까 K-5의 새로운 단어를 외워야함
    - K < 5 라면 0출력
1. 단어에서 알파벳에서 중복 & 'antic' 제외하고 비트마스크의 합을 구해 리스트 저장
2. K-5개의 단어를 조합해서 case를 구한뒤 해당 알파벳의 비스마스크 합을 구해 단어와 비교 
    - cnt의 최대 값을 ans에 갱신

'''

from itertools import combinations


def solve():
    global ans

    if K < 5:
        return

    for case in combinations(candidate, K-5):
        cs = 0
        cnt = 0

        for c in case:
            cs |= (1 << ord(c)-97)

        for ws in word_sum:
            if ws & cs == ws:
                cnt += 1

        ans = max(ans, cnt)


N, K = map(int, input().split())
core = set('antic')
word = [set(input()) - core for _ in range(N)]
candidate = set([c for w in word for c in w])
word_sum = []

for w in word:
    tmp = 0
    for c in w:
        tmp |= (1 << ord(c)-97)
    word_sum.append(tmp)

ans = -1e9

solve()

print(ans)
