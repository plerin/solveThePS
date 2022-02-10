

for _ in range(int(input())):
    lst = []
    for _ in range(2):
        lst.append(map(int, input().split()))

    s_y, s_k = map(sum, zip(*lst))
    print((('Yonsei', 'Korea')[s_y < s_k], 'Draw')[s_y == s_k])
