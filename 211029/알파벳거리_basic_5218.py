'''
[P]
길이가 같은 두 단어가 띄어쓰기로 구분되어 주어졌을 때 두 글자 x(앞), y(뒤) 사이의 알파벳 거리 구하기
    - x(B), y(D) 면 4-2=2 , 반대면 2+26-4=24
[S]
구현문제

[L]
1. split()으로 구분해서 A와 B로 구분
2. len()로 반복하며 알파벳 하나씩 계산 해서 ret에 담음 _ 계산은 ord()로 계산
'''

for _ in range(int(input())):
    ret = []
    a, b = input().split()

    for i in range(len(a)):
        if ord(b[i])-ord(a[i]) < 0:
            ret.append(26+ord(b[i])-ord(a[i]))
        else:
            ret.append(ord(b[i])-ord(a[i]))

    print('Distances:', *ret, sep=" ")
