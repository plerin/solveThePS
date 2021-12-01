'''
> P
0~9, +, - 총 12개 버튼인 리모컨에서 몇 개 고장난 버튼을 제외하고 원하는 n번으로 가는 최소 횟수
    - 고장난 버튼은 사용할 수 없다.
    - 현재 채널은 100번이다.
> S
브루트 포스 // 동적계획법

> L
1. 고장난 버튼(broken) list에 담아놔
2. n을 맨 앞에서 한 자리씩 반복문 진행
    -> if n not in broken then channel += str(n)
        else n-1 != 0 and n-1 not in broken then channel += str(n-1)
        else n+1 != 10 and n+1 not in broken than channel += str(n+1)
        ...
3. ret = (abs(channel - n + cnt), abs(n - 100))
'''

MAX = 500001


def moveChannel(target: int, broken: list):
    ret = abs(100-target)

    for num in range(MAX):
        # if list(map(lambda x: 1 if int(x) in broken else 0, str(num)))
        trigger = True
        for i in str(num):
            if int(i) in broken:
                trigger = False
                break
        if trigger:
            ret = min(ret, abs(target-num)+len(str(num)))

    return ret


N = int(input())
M = int(input())

if M:
    broken = list(map(int, input().split()))
else:
    broken = list()

ans = moveChannel(N, broken)

print(ans)
