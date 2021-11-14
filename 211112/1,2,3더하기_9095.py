'''
> P
1,2,3이 주어졌을 때 정수 n을 만드는 방법의 수를 구하라
> S
재귀
문제에서 전체 문제와 부분 문제의 단계를 파악
같은 함수를 사용해서 풀이 할건데 문제를 같은 형태의 작은 문제로 쪼개서 풀이
접근
    - param : arr(list)
    - bc : sum(arr) >= n -> if sum(arr) == n -> ret + 1
    - logic : append(i) // pop(i)
1. 재귀함수마다 1~3까지 들리는데 arr에 현재 값을 넣고 재귀 호출
'''


def recursive(n: int, arr: list = []):
    ret = 0
    if sum(arr) >= n:
        if sum(arr) == n:
            return 1
        return 0

    for i in range(1, 4):
        arr.append(i)
        ret += recursive(n, arr)
        arr.pop()

    return ret


def func2(total: int):
    global n
    ret = 0
    if total >= n:
        return 1 if total == n else 0

    for i in range(1, 4):
        total += i
        ret += func2(total)
        total -= i

    return ret


for _ in range(int(input())):
    n = int(input())
    ret = func2(0)
    print(ret)
