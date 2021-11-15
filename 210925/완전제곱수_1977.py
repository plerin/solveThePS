# import math

# M = int(input())
# N = int(input())

# S = math.ceil(M**0.5)
# E = math.floor(N**0.5)

# grp = list(map(lambda x: x**2, range(S, E+1)))

# if S <= E:
#     print(sum(grp), grp[0], sep='\n')
# else:
#     print('-1')


n, m = eval('int(input()),'*2)
grp = [i for i in range(n, m+1) if int(i**0.5)**2 == i] # 제곱근 확인 int(i**0.5)**2 == i
if grp:
    print(sum(grp), min(grp), sep='\n')
else:
    print('-1')
