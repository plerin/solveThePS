'''
일반식 : (A//(C-B))+1 IF >0 else -1
'''


def break_even_point(a, b, c):
    return a//(c-b)+1 if b < c else -1


A, B, C = map(int, input().split())

ret = break_even_point(A, B, C)

print(ret)
