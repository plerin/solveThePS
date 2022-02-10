


# n = int(input())
# a,b = 0,1

# if n<=1:
#     print(n)
# else:
#     for _ in range(n-2,-1,-1):
#         a,b = b,a+b
#     print(b)

# for _ in range(int(input())-1):
#     a,b = b,a+b

a,b=0,1;exec("a,b=b,a+b;"*int(input()));print(a)