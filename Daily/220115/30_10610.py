'''
>> P
양수 N을 입력받았을 때 포함된 숫자들을 섞어 가장 큰 30 배수를 구하라
    - 0으로 시작하지 않는다.
    - 존재하지 않으면 -1 출력
>> S
N을 입력 받고 순서를 바꿔 30의 배수 중 가장 큰 값을 출력하는 문제
30 배수 확인 방법
    - 모든 수의 합을 3으로 나눴을 때 나머지가 0이어야 한다(3의 배수여야 함)
    - 0이 있어야 한다


'''

N = list(input())
N.sort(reverse=True)
sumv = 0
if '0' not in N:
    print(-1)
else:
    for i in N:
        sumv += int(i)
    if sumv % 3 == 0:
        print(''.join(N))
    else:
        print(-1)
