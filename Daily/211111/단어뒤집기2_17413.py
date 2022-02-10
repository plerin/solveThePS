'''
> p
다양한 문자로 이루어진 문자열 s에서 단어만 뒤집어 출력
    - 단어 = 알파벳 소문자와 숫자로 이루어진 부분 문자열
> s
기초
stack 2개를 사용 _ origin(list) / rev(list) 숫자/문자 시작 ~ 구분자 나올 때까지
'''


def add(a, b):
    return a+b


def minus(a, b):
    return a - b


calc = {
    "add": add,
    "minus": minus
}

num1 = calc["add"](10, 5)
num2 = calc["minus"](10, 5)

print(num1, num2)
