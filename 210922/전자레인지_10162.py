def microwave(n):
    s1, r1 = divmod(n, 300)
    s2, r2 = divmod(r1, 60)
    s3, r3 = divmod(r2, 10)

    return (s1, s2, s3)


N = int(input())
if N % 10 == 0:
    ret = microwave(N)
    print(f'{ret[0]} {ret[1]} {ret[2]}')
else:
    print(-1)
# print(-1) if N%10 != 0 else print(f'')
# ret = -1 if N % 10 != 0 else microwave(N)
# print(ret)
