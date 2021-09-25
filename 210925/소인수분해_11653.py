def getPrime(n):
    lst = set(range(2, n+1))
    for i in range(2, n+1):
        lst = lst-set(range(i*i, n+1, i))

    return lst


def divide(n):
    grp = []

    while n != 1:
        for i in range(n+1):
            if n % i == 0:
                n //= i and grp.append(i)

    lst = []
    if n in prime_lst:
        lst.append(n)
        return lst

    for p in prime_lst[::-1]:
        if n % p == 0:
            lst.append(p) and divide(n/p)

    return lst


n = int(input())
prime_lst = getPrime(n)
ret = divide(n)
# print(ret)
for r in ret:
    print(r)
