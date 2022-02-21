'''
backjoon url -> https://www.acmicpc.net/problem/11729

>> Keyword
항상 어렵게 생각했던 하노이 정복.
규칙을 찾아 = 패턴이 보여 
N개를 1->3 으로 옮기려고 할 때
N-1개를 1->2 & 1개를 1->3 & N-1개를 2->3 으로 옮기는 것!
K = n개 횟수 = (n-1횟수 * 2) + 1 == 2**n - 1 

>> P
세 개의 장대가 있고 첫 번째 장대에 반경이 서로 다른 n개의 원판이 쌓여있다.
첫 번째 장대에서 세 번째 장대로 규칙에 따라 옮기려고 힐 떼
최소 이동 횟수를 갖는 경우를 출력하라

>> S
규칙을 찾자 
N개를 1-> 3으로 옮기려고 하면
1->2, N-1개 & 1->3, 1개 & 2->3 N-1개
N-1개를 1->2 옮기려고 하면
1->3, N-2개 & 1->2, 1개 & 3->2, N-2개

s(start), d(destination), t(temp)가 있고 개수는 N-1, 1, N-1개로 줄어든다.
반복되는 형태이니까 재귀로 풀어보자

접근
1. 옮긴 횟수(K)를 먼저 구하기
n개 횟수 = (n-1횟수 * 2) + 1 == 2**n - 1 
2. 재귀함수 호출
1. 재귀함수 선언
def hanoi_top(s: int, d:int, t:int, v:int) -> None:
    if v == 1:
        return
    hanoi_tap(s, t, d, v-1)
    print(s, d)
    hanoi_top(t, d, s, v-1)

'''


def hanoi_top(s: int, d: int, t: int, v: int) -> None:
    if v == 1:
        print(s, d)
        return
    hanoi_top(s, t, d, v-1)
    print(s, d)
    hanoi_top(t, d, s, v-1)


n = int(input())

print(2**n-1)

hanoi_top(1, 3, 2, n)
