'''
kp
#1. 함수화 해서 표출하기
#2. 리스트에서 가장 큰 인접한 점수 차이 계산
'''


def statistics(i, lst):
    n, *scores = lst
    maxv, minv = max(scores), min(scores)
    print(f'Class {i}')
    print('Max {0}, Min {1}, Largest gap {2}'.format(
        maxv, minv, maxv-minv))


for i in range(1, int(input())+1):
    statistics(i, map(int, input().split()))
