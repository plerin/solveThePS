
N = int(input())

for i in range(-N+1,N):
    print(' '*(abs(i))+'*'*(2*N-2*abs(i)-1))