'''
> P
수열 A가 주어졌을 때 가장 긴 증가하는 부분 수열을 구하는 프로그램 작성하라
> S
동적계획법 _ 최적해를 정하고 점화식을 구상 후 코드로 구현(dp 테이블 이용) + 하향식/상향식 고르고 + 반복이 많으면 재귀로 못 풀어 + 제한이 있어

11053 문제에 비해 dp에 기본 값을 [본인 값]로 주고 풀어보자
ai = 길이가 i인 수열에서 가장 긴 증가하는 부분수열 찾는 최적의 해, ki= 수열의 i번째 값
ai = max(ai, ai-1 + [k1], ai-2 + [k2], ... , ai-n + [kn])

dp 크기 : N+1, 초기값 [ki] 
'''


def bottomUp(n: int, seq: list):
    global dp

    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j] + [seq[i]], key=len)


N = int(input())
seq = list(map(int, input().split()))

dp = list(map(lambda x: [int(x)], seq))  # 현재 본인 값을 갖는 리스트로 초기화

bottomUp(N, seq)

print(len(max(dp, key=len)))
print(*max(dp, key=len))
