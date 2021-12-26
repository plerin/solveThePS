'''
>> P
N개의 단어는 알파벳 대문자로 구성되고 알파벳을 숫자로 매칭하여 단어들 합의 최대를 구하라
    - 알파벳은 고유 숫자로만 매칭
    - 단어의 포함된 알파벳은 최대 10개(0~9까지 매칭)
>> S
1. 알파벳이 어떤 숫자로 매칭되는 건 상관없어 단어 합의 최대값만 구하면 됨
2. 자리 수가 큰 알파벳은 큰 숫자(9부터 내림차순)으로 매칭되어야 함
3. 단어에 같은 알파벳이 여러 개가 들어갈 수 있어

알파벳 별 값을 주기위해 dict형태로 만들기
    - defaultdict(int)으로 기본 값 초기화
자리 수에 따른 값 갱신
    - 5자리 -> 10**5, 3자리 -> 10**3
같은 알파벳이 여러자리 들어갈 수 있어
    - 기존 값에 누적 -> 10010

>> F
1. 입력 받기(word)
2. word에서 각 단어를 탐색하며 alpha(dict) 갱신
3. 함수 호출
def cal_word()
    - vari : global ans(int) _ 결과 값 저장, global alpha(dict) _ 알파벳 별 가중치 저장
    - logic
        1) alpha.values()를 sorted(reverse=True)하고 변수에 저장
        2) 1의 결과값을 반복하며 내림차순(9->0)으로 지정
        3) ans 갱신
'''
from collections import defaultdict


def cal_word():
    global ans

    # 알파벳 중 값이 있는(0이 아닌) 값을 내림차순으로 반환
    alpha_val = sorted(list(alpha.values()), reverse=True)

    for idx, val in enumerate(alpha_val):   # 내림차순 순서대로 높은 숫자 할당(9->0)
        ans += val * (9 - idx)


N = int(input())
word = [input() for _ in range(N)]
alpha = defaultdict(int)
ans = 0

for w in word:
    for i in range(len(w)):
        alpha[w[i]] += 10 ** (len(w) - i - 1)   # 알파벳 자리에 맞는 가중치 할당(갱신)

cal_word()

print(ans)
