

N = int(input())
ret = 0
# 입력 받아 리턴
for i in range(1,N+1):
    ret += ((2*i*(2*i+1))//2 - (i*(i-1))//2)
# 이전 합 + sum(1~2n)-sum(1-(n-1))
print(ret)


# n=int(input());print(n*(n+1)*(n+2)//2)