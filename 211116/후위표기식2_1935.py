'''
> P
후위 표기식과 각 피연산자가 주어졌을 때 식 계산
> S
자료구조 유형
피연산자에 값을 매칭하여 stack을 활용하여 풀이함
접근
    1. 피연산자와 값을 어떻게 매칭? 
        - A-Z - ORD('A')로 해서 인덱스 0부터 시작해, 
    2. 연산자는 stack에 담고 식이 아오면 stack에서 값 2개 꺼내서 계산 후 다시 집어 넣어
        - 식이면 stack pop 2번  _> eval() 계산 -> append
'''

N = int(input())
arr = list(input())
arr_mat = [int(input()) for _ in range(N)]
stack = []

for c in arr:
    if c.isalpha():
        stack.append(arr_mat[ord(c)-ord('A')])
    else:
        a, b = stack.pop(), stack.pop()
        cal = eval(str(b)+c+str(a))
        stack.append(cal)

print(f'{stack[-1]:.02f}')
