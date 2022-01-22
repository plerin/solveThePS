'''
>> P
1~n까지 숫자인 n개 정점을 갖는 이진 트리가 주어지고
인오더와 포스트오더가 주어졌을 때 프리오더 구하시오
>> S
in_order : left - now - right
post_order : left - right - now 
pre_order : now - left - right

접근
1. None를 class로 만들고
2. in/post_order로 트리 만들기
3. 트리를 pre_order로 탐색 하며 출력

코드
1. 입력 받기
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
2. node class 생성
class node():
    def __init__(self):
        self.val = 0
        self.left = None
        slef.right = None
3. 함수 호출
ans = make_tree()

def make_tree(in_order: list) -> list:
    if in_order 
    Node(pop(0)
    while in_order:
        if len(in_order) >= 2:
            left = Node(in_order.pop())
            right = Node(in_order.pop())
        if len(in_order) == 1:
            left = Node(in_order.pop())
            right = None
        node.left = left
        node.right = right

4. pre_order로 출력

'''
tree
