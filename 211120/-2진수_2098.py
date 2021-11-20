'''
> P
10진법 수를 입력 받아 -2진수 출력하는 프로그램 작성
> S
수학
> L
10진수 n을 x진법으로 변환하는 방법 = while n: n//x 나누며 나머지를 모아서(ret = 나머지+ret) 반환한다
* keypoint
    1) 5 // -2 = -2가 나와야 하는데 -3이 나와 ,, // 연산은 기본적으로 내림을 하기 때문 => 그래서 만약 나머지가 있는경우 n값은 n // 2 + 1을 해줘야 함

'''


def convertFormat(n):
    if n == 0:
        return 0
    ans = ''

    while n:
        if n % (-2):
            # 나머지가 1인 경우 ==> '//' 연산이 기본적으로 내림이기 때문에 나머지를 양수로 만들어 주기 위해 +1을 해줘야 한다
            ans = '1'+ans
            n = (n//(-2)) + 1
        else:
            ans = '0'+ans
            n //= (-2)

    return ans


N = int(input())

ret = convertFormat(N)

print(ret)
