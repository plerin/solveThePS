'''
1부터 N까지 수를 이어쓸 때 자리 수를 구하는 방법

재귀 n을 입력하면 1이 될때까지 재귀를 타고 결과 반환

함수(continuesNum)
    - param : num:int, result:str
    - logic
        1) base-condition : if num == 1 then print result return
        2) func(num-1,result+=num)

'''


def continueNum(num: int, result: str = ''):
    if num == 0:
        return result

    return continueNum(num-1, str(num)+result)


def continueNum2(num: int):
    ans = ''

    for i in range(num, 0, -1):
        ans = str(i) + ans

    return ans


def continueNum3(num: int):
    ans = 0
    cnt = 1
    while num % 10:
        num, rest = divmod(num, 10)

        ans += rest * cnt
        cnt += 1

    return ans


N = int(input())

ret = continueNum3(N)

print(len(ret))
