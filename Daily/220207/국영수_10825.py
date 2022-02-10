'''
>> P
이름, 국어, 영어, 수학 점수가 주어질 때 조건에 따라 정렬하는 프로그램 작성

>> S

접근
sort(key=) or heapq로 풀이할 수 있어
단, 마지막 조건인 이름(str) 사전 순 증가를 어떻게 구현할 것인가? 
그냥 정렬하면 대 소문자르 모두 해결해줌
'''
import sys

input = sys.stdin.readline


def sort_student(arr: list) -> list:
    ret = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    return ret


N = int(input())
arr = [input().split() for _ in range(N)]

ans = sort_student(arr)

for student in ans:
    print(student[0])
