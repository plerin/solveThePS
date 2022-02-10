def compare(a, b):
    if a == b:
        return '=='
    elif a < b:
        return '<'
    elif a > b:
        return '>'


A, B = map(int, input().split())

ret = compare(A, B)

print(ret)
