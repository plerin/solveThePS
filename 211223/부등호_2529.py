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
        
'''


def match(comb: str, num: int):
    global arr

    if len(comb) == 0 or eval(comb[-2:]+str(num)):
        return True

    return False


def dfs(depth: int, comb: str):
    global visited, min_v, max_v

    if depth == K+1:
        if min_v == None:
            min_v = comb
        else:
            max_v = comb

    for i in range(10):
        if not visited[i] and match(comb, i):
            dfs(depth+1, comb+str(i))
    pass


K = int(input())
arr = input().split()
min_v, max_v = None, None
visited = [False] * 10  # 0~9 방문 체크

dfs(0, '')

print(mav_v, min_v, sep="\n")
