'''
>> P
K개 단어를 통해 읽을 수 있는 단어 최댓값 구하기
    - 모든 단어는 anta로 시작 tica로 끝난다(중복 없이 5개)
    - 단어는 영어 소문자로만 이루어져있고 길이는 8 <= x <= 15
    - 단어 중복은 없다
>> S
k < 5 면 return 0 -> 하나도 읽을 수 없어
antic를 제외하고 모든 단어를 모아놓고 K - 5 만큼 조합을 만들고 그 조합대로 단어의 모든 단어를 포괄하는 경우가 몇개인지?

일단 비트마스크를 다루는 방법부터
a = 12 (0b1100)
1. 포함 : a = a | (1<<1) -> 13 (0b1110)
2 .확인 : a & (1<<3) -> 8(True) // a & (1<<1) -> 0(False)
3. 제외 : a = a & ~(1<<3) -> 4 (0b0100)
4. 반전 _ 해당 위치 값을 바꿈 : a = a ^ (1<<3) -> 4 (0b0100) // a ^ (1<<0) -> 13(0b1101)

정리
1. K<5 면 print(0)하고 끝내버려
2. 입력 값을 통해 antic은 무조권 입력하고(영소문자 -> 숫자 -> 비트마스크 처리 _ False -> True)
3. K-5 개수만큼 그 외 모든 단어의 경우(combinations) 알파벳을 입력하고 몇개 까지 처리 가능한지 보기
    - 해당 단어의 알파벳이 모두 입력됐는지 확인 단어의 앞4개/뒤4개 자르고 해당 알파벳이 True인지 -> 맞으면 +1
        -> word[4:-4]

풀이
1. 모든 단어의 알파벳 중 antic를 뺀 나머지를 구한다
2. use_alpha = [False] * 26 _ 영소문자 26개를 false로 초기화
3. 'antic' 해당하는 순서는 True로 갱신
4. 나머지 알파벳으로 조합을 구해(combinations) -> 해당 알파벳을 켜(false->true)
5. 인식 단어 카운트 -> 최대 값 갱신
'''

from itertools import combinations


def use_library():
    global ans

    if K < 5:
        ans = 0
        return

    for case in combinations(alpha, K-5):
        now_sum = 0
        cnt = 0
        for c in case:
            now_sum |= (1 << ord(c)-97)

        for wb in word_sum:
            if wb & now_sum == wb:
                cnt += 1

        ans = max(ans, cnt)


N, K = map(int, input().split())
word = [set(input()) for _ in range(N)]
alpha = set([c for w in word for c in w]) - set('antic')
word_sum = []

for w in word:
    tmp = 0
    for c in w - set('antic'):
        tmp |= (1 << ord(c)-97)
    word_sum.append(tmp)

ans = -1e9
use_library()

print(ans)
