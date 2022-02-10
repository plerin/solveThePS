'''
>> P
부등호 개수(K)와 순서열(A)가 있고 0부터 9까지 숫자가 있을 때 부등호를 만족하는
최대 / 최소 숫자를 문자열로 출력하라
    - 0~9의 숫자가 중복되면 안됨
    - k의 범위는 2 ~ 9 
>> S
최대 값과 최소 값을 같이 구해야 한다.
    - min_v == None인 경우 min_v 갱신 아닌 경우 max_v에 갱신
0부터 시작하며 부등호에 맞지 않으면 건너뛰기(백트래킹)

2. 라이브러리 사용(permutations)
[0~9]으로 K+1자리 순열을 모두 구한뒤 부등호에 맞으면 입력 아니면 넘어가
    - min_v == None -> update else max_v update
>> F
def match(com:str, num: int):
    -vari : arr(list_global) _ 부등호를 갖고있음, 
    - 이전 값과 이전 부등호와 관계가 맞는지 확인후 안 맞으면 return False 맞으면 True
        -> if len(com) > 1 and eval(com[-2:]+str(num)) -> return True <-> return False

def dfs(depth: int, comb: str):
    - vari : visit(list_global) _ 0~9를 False로 갖고있어, min_v/max_v(str_global)
    - logic 
        1) base_condition : if depth == 3: -> ( if min_v == None -> min_v = comb <-> max_v = comb) & return
        2) for i in range(10) => if not visit[i] and match(i) -> dfs(depth+1, comb+str(i))

def use_library(num: int):
    - vari : comb(list_permutations으로 만들 것), min_v/max_v(str)
    - logic
        1) get comb using permutations
        2) check match with input arr
        3) update return value(min_v/max_v)
        4) return
'''
from itertools import permutations


# def use_library(num: int):
#     combs = permutations(range(10), num)
#     ret = [None, None]  # [min_v, max_v]
#     correct = True
#     for comb in combs:
#         for i in range(len(comb)-1):
#             if not eval(str(comb[i])+arr[i]+str(comb[i+1])):
#                 print(i, i+1, comb[i], comb[i+1])
#                 correct = False
#                 break

#         if correct == True:
#             if ret[0] == None:
#                 ret[0] = comb
#             else:
#                 ret[1] = comb

#     return ret


# def match2(depth: int, num: int):
#     global arr

#     if depth == 0 or eval(comb[-1]+arr[depth-1]+str(num)):
#         return True

#     return False


def match(a: int, b: int, op: str):
    if op == '<':
        return a < b
    elif op == '>':
        return a > b


def dfs(depth: int, comb: str):
    global visited, min_v, max_v

    if depth == K+1:
        if min_v == None:
            min_v = comb
        else:
            max_v = comb
        return

    for i in range(10):
        if visited[i]:
            continue
        if depth == 0 or match(int(comb[-1]), i, op[depth-1]):
            visited[i] = True
            dfs(depth+1, comb+str(i))
            visited[i] = False


K = int(input())
op = input().split()
min_v, max_v = None, None
visited = [False] * 10  # 0~9 방문 체크

dfs(0, '')
print(max_v, min_v, sep="\n")

# ans = use_library(K+1)
# print(*ans[::-1], sep='\n')
