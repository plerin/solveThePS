

n = int(input())

# for i in range(n):
#     print(' '*(n-i-1),'*'*(2*i+1),sep='')
# for j in range(n-1):
#     print(' '*(j+1),'*'*((2*n-3)-2*j),sep='')


for i in range(-n+1,n):
    print(' '*abs(i),'*'*(2*n-2*abs(i)-1))