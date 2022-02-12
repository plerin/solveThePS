'''
backjoon url -> https://www.acmicpc.net/problem/1339

>> Keyword
완전탐색, 순열 + 무언가 더 필요해(골드문제잖아) -> 가산점 부여
defaultdict()을 통해 알파벳 별로 점수 부여(자리 수에 따라 차등)
높은 점수부터 9부터 0까지 순서대로 부여하여 풀이

>> P
N개의 단어로 이루어져 있으며 단어는 알파벳 대문자로만 구성
알파벳 대문자를 0~9까지 숫자로 바꿔서 N개의 수를 합했을 때 가장 큰 값 만들어라
    - 알파벳과 숫자는 중복 없어야 함
>> S
모든 경우를 넣어봐야 하겠지만(범위도 작아 ~ 10) -> 완전탐색 
그래도 빠르게 찾기위한 아이디어가 필요해
기본적으로 자리수가 더 큰 수가 높은 숫자를 부여받아야 함
단어에 같은 알파벳도 여러 개 있을 수 있기 때문에 자리수에 대한 가산점 적용
    -> 'c'가 5,3번째 숫자 -> ['c'] += 10**4(5-1) += 10**2(3-2)

>>코딩
1. defaultdict으로 알파벳에 대한 가산점 준비
from collection import defa..
score_by_alpha = defaultdict(int)

2. 단어 순회하며 알파벳에 자리수에 따른 가산점 저장 
for _ in range(n):
    word = input()

    for i in range(len(word)):
        score_by_alpha[word[i]] += 10**i

3. dict items()를 내림차순 정렬후(기준 가산점) 하나씩 순회하며 9부터 차례대로 곱해주며 누적함
score_by_alpha.items().sort() -> 결과가?

'''
from collections import defaultdict


def get_maximum(score: dict) -> int:
    ret = 0
    cnt = 9
    for score in sorted(list(score.values()), reverse=True):
        ret += score * cnt
        cnt -= 1
    return ret


n = int(input())
score_by_alpha = defaultdict(int)

for _ in range(n):
    word = input()
    word = word[::-1]

    for i in range(len(word)):
        score_by_alpha[word[i]] += 10**i

print(get_maximum(score_by_alpha))
