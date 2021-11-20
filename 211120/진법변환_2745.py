'''
> P
B진법 N이 주어졌을 때 10진법으로 바꿔 출력하는 프로그램 
> S
수학
> L
x진법 수를 10진법으로 변환하는 과정 
    1. for n in num[::-1]
    2. ans += n*a // a *= a
    3. if n.isalpha() then ord(n) - 55
'''


def convFormat(n, b):
    ans = 0

    for i in range(len(n)):
        num = ord(n[i])-55 if n[i].isalpha() else int(n[i])
        ans += (b**i) * num

    return ans


N, B = input().split()

ret = convFormat(N[::-1], int(B))

print(ret)
