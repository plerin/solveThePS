# n = int(input())
# star = list(map(lambda x: '*'*x,range(1,n+1)))
# blank = list(map(lambda x: ' '*x,range(n-1,-1,-1)))

# # print(''.join({}).format(*zip(blank,star)),sep='\n')
# for elem in zip(blank,star):
#     print(''.join(elem),end='\n')


n = int(input())

for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)
