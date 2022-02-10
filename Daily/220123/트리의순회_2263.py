'''
>> P
1~n까지 n개 정점을 갖는 이진트리가 주어진다.
인오더와 포스트오더가 주어졌을 때 프리오더 구하는 프로그램 작성

>> S
인오더와 포스트오더의 특징을 이용해서 프리오더를 구하라
인오더 = LPR, 루트가 중간에 나오고 왼쪽 먼저 탐색
포스트오더 = LRP, 루트가 맨 마지막에 나오고 왼쪽 먼저 탐색
프리오더 = PRL, 루트가 맨 처음 나오고 L,R 순서대로 탐색
-> 인오더, 포스트오더를 활용해서 루트를 찾고 좌,우 서브트리를 찾은 뒤
1) print(root)
2) left subtree recursive call
3) right subtree recursive call

접근
1) 후위 순회 끝값(루트)값이 중위 순회의 어디인지 인덱스 확인하기 위해 중위순회 값의 인덱스 저장
    (중위 순회는 루트를 기준으로 left/right 서브쿼리가 구분되기 때문)
2) 프리오더 순서 구하는 함수 선언
    - param : in_start, in_end, post_start, post_end
    - basc_condition : start > end
    - logic
        1) find root(parent) = post[post_end] & print
        2) left, right 
            left = position[parent] - in_start
            right = in_end - position[parent]
        3) recursive call
            preorder(in_start, in_start+left-1, post_start, post_start+left-1)
            preorder(in_end-right+1, in_end, post_start-right, post_end-1)
'''


import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def preorder(in_start: int, in_end: int, post_start: int, post_end: int) -> None:
    if (in_start > in_end) or (post_start > post_end):
        return

    # parent 찾아 출력
    parent = post_order[post_end]
    print(parent, end=' ')

    # left / right 서브쿼리 기준 잡기
    left = position[parent] - in_start
    right = in_end - position[parent]

    # 왼쪽 서브 쿼리는 in_order와 post_order가 같다 == in_order는 루트 기준으로 나뉘기 때문에 in_start ~ in_start+left-1(parent 1개 뺌) && post도 마찬가지
    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    # 오른쪽 서브 쿼리는 in_order와 post_order가 달라 -> parent위치 때문에
    # in_oder는 start + 1 해주고 in_end 반명(parent가 배열 중간에 있어서)
    # post_order는 -right 해주고 pest_end-1 반영(parent가 맨 뒤에 있어서)
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)


if __name__ == '__main__':

    n = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))

    # position 찾기 _ root index 찾기 위해
    position = [0] * (n+1)
    for i in range(n):
        position[in_order[i]] = i

    preorder(0, n-1, 0, n-1)
