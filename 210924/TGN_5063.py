


# n = int(input())

# for _ in range(n):
#     a,b,c = map(int, input().split())
#     if (a+c)<b: print('advertise')
#     elif (a+c)>b: print('do not advertise')
#     else: print('does not matter')



for _ in range(int(input())):
    a,b,c = map(int, input().split())
    print(((('','do not')[a+c>b]+'advertise'),'does not matter')[a+c==b])