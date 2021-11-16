'''
> P
문자열 N개가 주어질 때 조건에 맞는 개수를 공백을 구분자로 출력하라
> S
구현 
접근
    1. 한 문자씩 조건 맞도록 카운팅
'''
# import sys

# str = sys.stdin.readlines()

# print(str)

while True:
    str = input()
    if not str:
        # exit()
        break

    ret = [0 for _ in range(4)]

    for c in str:
        if c.isspace():
            ret[3] += 1
        elif c.isdigit():
            ret[2] += 1
        elif c.isupper():
            ret[1] += 1
        else:
            ret[0] += 1

    print(*ret)

# print(input())

# while input():
#     print('go')
