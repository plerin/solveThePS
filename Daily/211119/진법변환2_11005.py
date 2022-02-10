'''
> P
10진수 N을 B진법으로 바꿔 출력
    - 10~35까지는(A~Z)
> S
수학(기초)
> L
진법 구하는 방식을 적용 10부터 35는 A~Z까지로 매칭 
    - if 나머지가 10보다 크면 chr(n+55)
'''


def convertFormat(n, b):
    ret = ''

    while n:
        n, rest = divmod(n, b)
        if rest >= 10:
            ret += chr(55+rest)
        else:
            ret += str(rest)

    return ret[::-1]


N, B = map(int, input().split())

ret = convertFormat(N, B)

print(ret)
