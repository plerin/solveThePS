'''
>> P
+,-,괄호 를 사용하여 식을 만들고 괄호를 지웠다.
괄호를 적절히 사용하여 식의 최소 값을 구하라
    - 수는 0으로 시작할 수 있음
>> S
기본 아이디어는 '-'/'+'가 같이 있는가 둘 중 하나만 있는가에 따라 달라
    - 둘 중 하나만 있는 경우는 그냥 더해주면 풀림
    - 두개 모두 있는 경우는 달리 처리해야 함
        -> 이 문제에서 포인트

1. '-'를 기준으로 나누어준다.
2. 맨 앞에 기호가 '+'인 경우와 '-'에 따라 다르게 처리
    - '+'인 경우는 해당 값을 더해줘야함(+)
    - '-'인 경우는 더해준 값을 모두 빼주면 됨


>> C
1. 입력 받는다.
exp = input()

2. 함수 호출
ans = solve()

def solve() -> int:
    global ans
    div_exp = exp.split('-')

    ret = 0
    first_exp = PLUS if exp.isdigit() else MINUS
    
    for part in div_exp:
        ret += exec(part)
    
    return ret

3. 결과 출력
print(ans)
'''


def solve() -> int:
    div_exp = exp.split('-')
    ret = 0

    # 2가지 경우로 나뉘어 맨 앞 숫자가 - 붙은 경우 아닌 경우
    # 붙은 경우는 그냥 그대로 처리하면 됨
    # 안 붙은 경우는 뒤랑 다르게 처리해야 함

    if not div_exp[0]:  # 맨 앞자에 '-'가 있는 경우
        for idx in range(1, len(div_exp)):
            part = 0
            for num in div_exp[idx].split('+'):
                part += int(num)
            ret -= part
    else:   # 맨 앞자리에 '+'가 있는 경우
        for idx in range(len(div_exp)):
            part = 0
            for num in div_exp[idx].split('+'):
                part += int(num)
            if idx == 0:
                ret += part
            else:
                ret -= part

    return ret


def short() -> int:
    div_exp = exp.split('-')
    ret = 0
    for i in div_exp[0].split('+'):
        ret += int(i)
    for i in div_exp[1:]:
        for j in i.split('+'):
            ret -= int(j)

    return ret


exp = input()

ans = short()

print(ans)
