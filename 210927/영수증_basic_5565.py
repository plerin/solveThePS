# from collections import deque


# total = int(input())

# books = deque([map(int,input()) for _ in range(9)])

# while True:
#     sum_p = sum(books[:-1])
#     if sum_p == total: 
#         print(total[-1])
#         break
#     else:
#         books.rotate(-1)


total = int(input())
sum_p = sum([int(input()) for _ in range(9)])
print(total-sum_p)