'''
> p
문장이 주어졌을 때 단어를 모두 뒤집어 출력
> s
구현
1. 문장을 space로 구분하여 리스트로 받아
2. 리스트 컴프리헨션으로 단어를 뒤집고 join으로 출력
'''
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().split()
    print(' '.join(list(map(lambda x: x[::-1], s))))
