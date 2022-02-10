'''
>> In
내가 못 풀고 다른 사람의 풀이를 먼저 봤는데 반성되는 부분 하나와 명심할 부분 하나
반성 1. 골드문제라서 풀어볼 생각 자체를 안 했다는 것 -> 골드 문제를 풀 수 있어야 PS라는 산을 넘어갈 수 있다.
명심 1. 못 푼 것, 안 푼 것 둘 다 괜찮아 내가 할 일을 다른 사람의 풀이를 봤다는 건 내 것으로 만들어야 한다는 말
        그러니 그 풀이 방법을 습득하려고 노력하자(처음부터 구상부터 따라갈 수 있도록 -> 풀이만 보고 붙여넣는게 아니라)
>> P
N개의 단어가 알파벳으로 이루어져 있을 때 알파벳에 숫자를 할당하여 N개 단어 합의 최대 값을 구하라
    - 알파벳은 대문자로만 으루어져 있다.
    - 알파벳은 오직 하나의 숫자만(중복없이) 할당됨
>> S
자리 수에 따라 큰 값이 할당되어야 함
    - 5자리라면 5번째 자리의 수가 9 4번째 자리 수가 8 이런 식으로
        -> 알파벳의 자리 순서에 따라 값을 지정 1,3 자리에 있으면 101(100+1)
        -> dic 자료형으로 알파벳별 기본 값을 0으로 초기화 -> 이후 갱신
    - 큰 값부터 읽으며 * 9부터 0까지 수를 할당
    => 어떤 알파벳에 어떤 값이 할당됐는지 중요하지 않아 중요한건 최대 값

>> F
alpha = defaultdict(int) -> 어떤 key(알파벳)을 갖던 value 기본 값은 0
word = [input() for _ in range(N)]
def get_maximum_val():
    - vari : global alpha(dict), use_alpha = set() _사용된 알파벳 저장
    - logic
        1) for w in word
            => for i in range(len(w))
                => alpha[w[i]] += 10 ** (len(w) - i - 1) & use_alpha.add(w[i])
        2) 사용된 알파벳의 값을 리스트에 저장
            for a in use_alpha:
                => use_alpha_val.append(alpha[a])
        2) 알파벳 개수만큼 반복하며 숫자 할당(9부터 0까지)
            for a in sorted(use_alpah_val, reverse=True):
                => ans += a * (9 - i)
'''

from collections import defaultdict


def get_maximum():
    global ans

    alpha = defaultdict(int)

    for w in word:
        for i in range(len(w)):
            alpha[w[i]] += 10 ** (len(w) - i - 1)   # 알파벳 자리에 따른 값 갱신(n자리면 10**n 더하기)

    alpha_val = sorted(list(alpha.values()), reverse=True)  # 큰 값부터 사용하기 위한 정렬

    for idx, val in enumerate(alpha_val):
        ans += val * (9 - idx)  # 큰 값부터 9부터 0까지 순서대로 부여(알파벳->숫자)


N = int(input())
word = [input() for _ in range(N)]
ans = 0

get_maximum()

print(ans)
