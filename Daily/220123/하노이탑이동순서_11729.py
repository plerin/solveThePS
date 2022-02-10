'''
>> P
3개의 장대와 반경이 서로 다른 n개 원판이 있을 때
1번 -> 3번 장대로 규칙에 따라 최소 횟수로 옮길 때 횟수와 과정을 출력하라
    - 규칙
        1) 한 번에 한 개의 원판 이동
        2) 원판은 항상 위의 것이 아래 것보다 작아야 함
>> S
구해야 하는 것 : 횟수 / 과정

규칙
N개를 1 -> 3으로 옮기는 과정
1) N-1개 1 -> 2
2) 1개 1 -> 3
3) N-1개 2 -> 3
from, to, tmp으로 매칭하여 풀이 함

접근
1) 과정 출력 _ dfs사용
    - 1개의 문제를 3개의 문제로 나눈다 == 분할 정복
def hanoi(fm, to, tmp, num):
    if num == 1:
        print(fm, to)
    else:
        hanoi(fm, tmp, to, num-1)
        print(fm, to)
        hanoi(tmp, to, fm, num-1)
2) 횟수
d(n) = n개를 이동하는 횟수
d(n) = 2*d(n-1) + 1, d(1) = 1
cnt = 1
for i in range(n-1):
    cnt = cnt * 2 + 1

'''


def hanoi(fm: int, to: int, tmp: int, num: int) -> None:
    if num == 1:
        print(fm, to)
        return

    # 분할 정복 1개 문제 -> 3개로 나눠풀기
    hanoi(fm, tmp, to, num-1)
    print(fm, to)
    hanoi(tmp, to, fm, num-1)


if __name__ == '__main__':
    N = int(input())

    # 횟수 _ DP 방식
    cnt = 1
    for i in range(N-1):
        cnt = cnt * 2 + 1
    print(cnt)

    # 과정
    hanoi(1, 3, 2, N)
