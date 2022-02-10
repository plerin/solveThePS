import heapq


def heapsort(iter):
    h = []
    ret = []
    for i in iter:
        heapq.heappush(h, i)
    while h:
        ret.append(heapq.heappop(h))
    return ret


ret = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(ret)
