'''
kp
#1. 알파벳 매칭 형태를 list/dictionary로 잡아둔다
#2. 알파벳을 하나씩 스택에 담고 현재 들어온 값과 이전 값과 매칭하며 있으면 pop하고 count+=1 , 결과 끝나고 stack에 남은 건 하나당 count+1
    [-1]과 비교하고 맞으면 POP빼고 WHILE로 [-1]로 또 비교해봐 STACK이 비어있지 않을 때까지

#1. 변수 선언 및 입력
    1) alphabet : 입력 받은 문자의 알파벳을 하나씩 담을 리스트 선언
    2) 입력 받은 문자를 각 알파벳 단위로 반복문
#2. 로직
    1) alphabet에 담겨 있는 동안 반복문(while)
    2) 현재 문자와 alpha 마지막 문자([-1])와 비교하여 매칭테이블에 있는지 확인
    3) 있다면 pop해서 묶고나서 2번 과정을 반복
    4) 이제 없다면 cnt+1하고 넘어감
    5) 문자 반복이 끝나면 스택에 남은 개수만큼 cnt에 더해서 반환
'''

ret = 0
stack = []

conv_table = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in input():
    while stack and stack[-1]+c in conv_table:
        c = stack.pop()+c

    if len(c) == 1:
        stack.append(c)
    else:
        ret += 1
        ret += len(stack)
        stack = []

ret += len(stack)

print(ret)
