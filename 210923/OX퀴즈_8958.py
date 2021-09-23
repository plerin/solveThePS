



n = int(input())
ret = [0 for _ in range(n)];

for i in range(n):
    # 퀴즈 결과 입력 받고 split('X')인 arr case
    case = input().split('X')
    # ret 에 for문 sum값 더하기 
    ret[i] = sum([len(g)*(len(g)+1)//2 for g in case])

# ret 출력 

for r in ret:
    print(r)