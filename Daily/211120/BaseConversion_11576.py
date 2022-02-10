'''
> P
A진법을 B진법으로 변환시켜주는 프로그램 개발
    - 진법은 2~30이하 
    - 
> S
수학
> L
풀이
    1. a진법을 10진수로 나타내고 
    2. 10진수를 b진법으로 나타낸 결과 출력
'''


def convDecimal(arr, base):
    ans = 0

    for i in range(len(arr)):
        ans += (base**i) * arr[i]
        # num = ord(arr[i])-48 if arr[i].isalpha() else int(arr[i])
        # ans += (base**i) * num

    return ans


def convBase(decimal, base):
    if decimal == 0:
        return [0]

    ans = []

    while decimal:
        decimal, rest = divmod(decimal, base)
        ans.append(str(rest))

    return ans


A, B = map(int, input().split())
m = int(input())
base_a = list(map(int, input().split()))

decimal = convDecimal(base_a[::-1], A)
ret = convBase(decimal, B)

print(' '.join(ret[::-1]))
