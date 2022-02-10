'''

ai = i잔 포도주를 마실 수 있는 최대 값(최적해)
    - 연속 3잔 이상 마실 수 없어

1잔 추가 => 마시거나 / 안마시거나
2잔 추가 -> 앞잔 마시거나 / 뒷잔 마시거나 / 둘다 마시거나
3잔 추가 -> 앞 2잔 마시거나 / 뒷 2잔 마시거나 / 1,3 마시거나 
이렇게 보면 
2잔에서 앞잔 마시거나 / 뒷잔 마시거나 => 1잔의 경우와 중복 => 둘다 마시거나만 남아
3잔엥서 앞/뒤 2잔 마시거나 => 2잔의 모두 마신다와 중복 // 1,3 마시거나 => 1잔의 내용과 중복
==> 2잔으로 보면 3가지 경우만 존재 나머지는 중복(부분 문제 풀이가능)

d(i) = max(d(i-3) + seq[i-1] + seq[i], d(i-2) + seq[i], d(i-1))
=> 최근 2잔 모두 마시는 경우 / 최근 1잔 마시는 경우 / 최근 1잔 안 마시는 경우
'''
import sys

input = sys.stdin.readline

MAX = 10000


def maxDrink(n: int, amount: list):
    dp = [0 for i in range(MAX)]

    dp[0], dp[1] = amount[0], amount[0]+amount[1]
    dp[2] = max(amount[0]+amount[2], amount[1]+amount[2], dp[1])

    for i in range(3, MAX):
        dp[i] = max(dp[i-3] + amount[i-1]+amount[i],
                    dp[i-2] + amount[i], dp[i-1])

    return dp[n-1]


n = int(input())
amount = [int(input()) for _ in range(n)] + [0 for _ in range(MAX-n)]

ret = maxDrink(n, amount)

print(ret)
