

# 게임 횟수 입력
N = int(input())
sco = [100 for _ in range(2)]

# 횟수만큼 반복문 돌며 게임 결과 입력
for n in range(N):
    a, b = map(int, input().split())
    if a == b: continue
    
    if b > a:
        sco[0] = sco[0]-max(a, b)
    else:
        sco[1] = sco[1]-max(a, b)

# 결과 출력 [0],[1] ,set='\n'
print(sco[0], sco[1], sep='\n')
