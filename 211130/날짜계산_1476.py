'''

전략
1. 1부터 1씩 큰 수를 입력
2. 날짜를 계산
3. 입력 값(날짜)와 같으면 출력 후 종료
'''


def calDate(day: int):
    E = day % 15 if day % 15 != 0 else 15
    S = day % 28 if day % 28 != 0 else 28
    M = day % 19 if day % 19 != 0 else 19
    return (E, S, M)


E, S, M = map(int, input().split())

num = 0
while True:
    num += 1
    if (E, S, M) == calDate(num):
        print(num)
        break
