'''
> P
수빈이는 N명의 동생과 숨바꼭질
수빈이(x)는 1초 뒤 x+D, x-D로 움직일 수 있을 때 모든 동생을 찾기 위한 D 값 중 최댓값을 구하라
> S
수학
> L
1. 수빈이와 동생들간의 거리를 구하고 이 거리들(최소거리,최대거리)간의 GCD를 구하기
'''

# 수빈이와 동생 위치 차이간의 최대공약수를 구하는 문제
# 2개 이상의 수에 대해 최대 공약수 구하는 방법은 한 수는 한 값으로 초기화하고(ret = min(diff)) 다른 모든 수와 ret의 gcd를 구하는 것(ret = getGCD(ret, d))


def getGCD(a, b):
    return b if a % b == 0 else getGCD(b, a % b)


N, S = map(int, input().split())
diff = list(map(lambda x: abs(S - int(x)), input().split()))
ret = min(diff)

for d in diff:
    ret = getGCD(ret, d)

print(ret)
