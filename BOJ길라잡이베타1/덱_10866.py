'''

'''

import sys

input = sys.stdin.readline

# N = int(input())
# deque = []

# for _ in range(N):
#     cmd = input()
#     if cmd.startswith("push_front"):
#         deque.insert(0, int(cmd.split()[1]))
#     elif cmd.startswith("push_back"):
#         deque.append(int(cmd.split()[1]))
#     elif cmd.startswith("pop_front"):
#         output = deque.pop(0) if len(deque) != 0 else -1
#         print(output)
#     elif cmd.startswith("pop_back"):
#         output = deque.pop() if len(deque) != 0 else -1
#         print(output)
#     elif cmd.startswith("size"):
#         print(len(deque))
#     elif cmd.startswith("empty"):
#         output = 1 if len(deque) == 0 else 0
#         print(output)
#     elif cmd.startswith("front"):
#         output = deque[0] if len(deque) != 0 else -1
#         print(output)
#     elif cmd.startswith("back"):
#         output = deque[-1] if len(deque) != 0 else -1
#         print(output)


def push_front(x, deq):
    tmp = [x]
    tmp.extend(deq)
    deq = tmp
    return deq


def push_back(x, deq):
    deq.append(x)
    return deq


def pop_front(deq):
    if deq:
        print(deq.pop(0))
    else:
        print(-1)


def pop_back(deq):
    if deq:
        print(deq.pop())
    else:
        print(-1)


def size(deq):
    print(len(deq))


def empty(deq):
    if deq:
        print(0)
    else:
        print(1)


def front(deq):
    print(deq)
    if deq:
        print(deq[0])
    else:
        print(-1)


def back(deq):
    if deq:
        print(deq[-1])
    else:
        print(-1)


statement_dict = {
    'push_front': push_front,
    'push_back': push_back,
    'pop_front': pop_front,
    'pop_back': pop_back,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back
}

N = int(input())
deq = []

for _ in range(N):
    statement = input().split()

    if len(statement) == 1:
        command = statement[0]
        statement_dict[command](deq)
    else:
        command, x = statement
        deq = statement_dict[command](x, deq)
