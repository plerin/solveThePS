

A, B = map(int, input().split())
ret = ''
carry = 0

while A or B or carry:
    ar, br = A % 10, B % 10
    A, B = A//10, B//10

    s, r = divmod(ar+br+carry, 10)
    carry = s
    ret += str(r)

print(int(ret[::-1]))
