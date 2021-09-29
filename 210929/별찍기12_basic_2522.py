N = int(input())
for i in range(-N+1,N):
    print(' '*abs(i)+'*'*(N-abs(i)))
    # print('{0:>N}'.format('*'*(N-abs(i))))