'''
>> P
N개 수가 주어졌을 때 오름차순으로 정렬하는 프로그램 작성
    - 범위 : 개수 / 절댓값 ~ 100만 
    - 중복 : x
>> S
1. 그냥 정렬하면 안되나? 
2. 이진탐색으로 하면? 그게 퀵정렬보다 빠른가? 
    - 입력을 받을 때마다 배열에서 들어갈 위치에 입력(bisect_left)
'''
import sys

input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]

arr.sort()

print(*arr, sep='\n')
