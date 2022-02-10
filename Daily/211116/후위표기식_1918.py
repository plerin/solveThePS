'''
> P
중위 표기식을 후위 표기식으로 변환하라 
> S
자료구조 _ stack
접근
    1. 숫자 나오면 출력
    2. '(' 나오면 push
    3. 사칙연산(+ - * /)가 나오면 자신보다 우선순위가 높은 것 출력 
    5. ')' 나오면 여는 괄호 나올 때까지 pop 하여 출력
'''

arr = list(input())
stack = []
ret = []

priority = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

for c in arr:
    if c.isalpha():
        ret.append(c)
    elif c == '(':
        stack.append(c)
    elif c in ('*', '/', '+', '-'):
        while stack and priority[c] <= priority[stack[-1]]:
            ret.append(stack.pop())
        stack.append(c)
    else:
        while stack[-1] != '(':
            ret.append(stack.pop())
        stack.pop()

while stack:
    ret.append(stack.pop())

print(*ret, sep='')
