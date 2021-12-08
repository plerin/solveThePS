'''
> P
0~9 숫자를 부등호에 만족하는 수를 문자열로 반환하라
    - 최대 / 최소 값 모두 반환
    - 수는 모두 달라야 한다

> S
1. 최대 / 최소에 따라 정렬 후 재귀로 구하기
    - 최대 -> 내림차순 정렬 후 // 최소 -> 오름차순 정렬
2. 가저 조건(base-condition)
    - 모인 숫자 수가 n+1이면 입력된 부등호에 대입하며 맡는 경우 return 
3. 함수만들기
    def get_correct_str
        - param : start(int) _ 현재 수, choose(list) _ 선택된 수
        - vari : global sign(list)
'''


# def get_correct_str(depth: int, choose: str, direct: list):
#     global f, sign
#     ret = ''

#     if depth == k+1:
#         if eval(choose) == True:
#             print(''.join(list(filter(lambda x: x.isdigit() == True, choose))))
#             return True
#         return False

#     for i in direct:
#         if str(i) in choose:
#             continue
#         if depth != 0 and eval(choose[-2:]+str(i)) == False:
#             continue
#         ret = get_correct_str(depth+1, choose+str(i)+sign[depth], direct)

#         if ret == True:
#             return True


# k = int(input())
# sign = list(map(str, input().split())) + [' ']
# get_correct_str(0, '', range(9, -1, -1))
# get_correct_str(0, '', range(10))


n = int(input())
op = input().split()
check = [False] * 10
mx, mn = "", ""


def possible(a, b, k):
    if k == '<':
        return a < b
    if k == '>':
        return a > b
    # return True


def solve(cnt, s):
    global mx, mn

    if cnt == n+1:
        if len(mn) == 0:
            mn = s
        else:
            mx = s
        return

    for i in range(10):
        if check[i] == False:
            if cnt == 0 or possible(int(s[-1]), i, op[cnt-1]):
                check[i] = True
                solve(cnt+1, s+str(i))
                check[i] = False


solve(0, "")
print(mx)
print(mn)
