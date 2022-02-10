

n = int(input())

# print(1 if (n % 4 == 0 and n % 100 != 0) or (
#     n % 4 == 0 and n % 400 == 0) else 0)


print(1 if (n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)) else 0)
