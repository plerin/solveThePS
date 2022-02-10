# n = int(input())
# for i in range(1, 10):
#     print('{} * {} = {}'.format(n, i, (n*i)))


i = int(input())
j = 1
exec("print(i,'*',j,'=',i*j);j+=1;"*9)
