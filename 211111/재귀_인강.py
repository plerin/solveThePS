# n ~ 1 까지 출력 _ 재귀를 이용하라

# def doRecursive(arr: list):
#     if len(arr) == n:
#         return arr

#     for i in range(n, 0, -1):
#         if i in arr:
#             continue

#         arr.append(i)
#         return doRecursive(arr)


# n = 100
# ret = doRecursive([])
# print(ret)


def func1(n: int):
    if n == 0:
        return       # 기저 조건(재귀 함수가 끝나기 위한 조건)
    print(n, end=' ')       # 로직 처리
    func1(n-1)              # 재귀 함수 호출(기저 함수 도달할 수 있도록)


func1(100)


# 1~n까지의 합 _ 재귀를 이용
'''
위와 같은 방법으로 구현 가능
param : arr(list)
logic : len(arr)이 n이 될 때까지 n을 더해줘
'''


# def func(arr: list = []):
#     if len(arr) == n:
#         return arr

#     for i in range(len(arr)+1, n+1):
#         if i not in arr:
#             arr.append(i)
#             return func(arr)


def func2(n: int):
    # 기저 조건
    if n == 0:
        return 0
    # 로직
    # 재귀 호출
    return n + func2(n-1)


print(func2(100))
# n = 100
# ret = func()

# print(ret)


# 재귀 함수의 조건
# 특정 입력에 대해서는 자기 자신을 호출하지 않고 종료되어야 함(base condition) , 모든 입력은 base condition으로 수렴해야 함