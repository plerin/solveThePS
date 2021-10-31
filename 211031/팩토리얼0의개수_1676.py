# from math import factorial


# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)


# N = int(input())

# ret = 0
# for i in str(factorial(N))[::-1]:
#     if i != '0':
#         break
#     ret += 1

# print(ret)


import sys
input = sys.stdin.readline

ret = 0

N = int(input())

while N >= 5:
    ret += N//5

    N //= 5

print(ret)
