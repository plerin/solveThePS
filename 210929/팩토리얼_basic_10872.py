
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


N = int(input())
ret = factorial(N)
print(ret)