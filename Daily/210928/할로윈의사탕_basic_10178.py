

for _ in range(int(input())):
    candy, child = map(int,input().split()) 
    share, rest = divmod(candy,child)
    print(f'You get {share} piece(s) and your dad gets {rest} piece(s).')