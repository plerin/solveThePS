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

MAX = 1000001


def moveChannel(target: int, broken: list):
    # 기존 채널(100)에서 이동하는 경우를 초기값으로 지정
    ret = abs(100-target)

    # 0에서 50만 가는 경우(50만) + 50만1~100만에서 50만 가는 경우(50만) = 100만
    for num in range(MAX):
        trigger = True
        for i in str(num):
            # 현재 숫자에서 부서진 버튼 채널이 존재하면 생략
            if int(i) in broken:
                trigger = False
                break
        # 부서진 번호가 없는 숫자인 경우
        if trigger:
            ret = min(ret, abs(target-num)+len(str(num)))

    return ret


N = int(input())
M = int(input())

# 부서진 버튼이 있는 경우만 입력 받음
if M:
    broken = list(map(int, input().split()))
else:
    broken = list()

ans = moveChannel(N, broken)

print(ans)
