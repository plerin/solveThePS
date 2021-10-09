def dp(n):
    d[1] = 1
    d[2] = 2

    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2]) % 10007

    return d[n]


N = int(input())

d = [0] * (1001)
ret = dp(N)

print(ret)
