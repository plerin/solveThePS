'''
>> P
이진 트리를 입력받아 전위(pre) / 중위(in) / 후위(post) 순회 결과를 출력하라
    - 전위 : root먼저 -> l -> r
    - 중위 : l -> root -> r
    - 후위 : l -> r -> root

>> S
node(class)를 만들고 입력 받은 값으로 초기화하자
    - def __init__(self, data, left_node, right_node)
    - .이면 None으로 처리하기 -> if left_node == '.' then left.node = None
전위/중위/후위 모두 함수만들기
    - root 출력이 언제인지 판단하기
'''


class Node():
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def pre_order(node):
    print(node.data, end='')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])


def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None:
        in_order(tree[node.right_node])


def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end='')


N = int(input())
tree = {}

for _ in range(N):
    data, left_node, right_node = input().split()

    if left_node == '.':
        left_node = None
    if right_node == '.':
        right_node = None

    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
