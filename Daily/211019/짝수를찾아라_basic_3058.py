'''
kp
#1. 짝수만 리스트로 추려서 한 번에 출력
'''
for _ in range(int(input())):
    even = sorted(list(filter(lambda x: x %
                              2 == 0, map(int, input().split()))))
    print(sum(even), even[0])
