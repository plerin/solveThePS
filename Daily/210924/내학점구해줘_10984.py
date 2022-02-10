

# 총 n번 반복 
    # 총 m번 반복
        # a,b를 받고, sum(a) , round(sum(b)/len(b),1) -> print

for _ in range(int(input())):
    sn,sa,cnt = 0,0,0
    for _ in range(int(input())):
        n, a = input(int, input().split())
        sn, sa= sn+n, sa+a
        cnt += 1
    print(f'{sn} {round(sa/len(cnt),1)}')