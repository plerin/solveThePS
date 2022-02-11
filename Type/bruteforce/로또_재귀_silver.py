'''
backjoon url : https://www.acmicpc.net/problem/6603

>> Keyword
완전탐색, 가장 기본적인 재귀 - 반복하며 리스트에 없는 값을 하나씩 추가 

>> P
1~49에서 수 6개를 고른다.
k개를 골라 집한 S를 만든 다음 그 수만으로 경우의 수 만드는 것 
집한 S와 k가 주어졌을 때 수 고르는 모든 방법 구하라
    - S 원소는 오름차순으로 주어진다.
    - 입력 마지막 줄에는 0이 주어진다.

>> S
S집합에서 6개 경우의 수를 구해아함
완전탐색 기억을 되살려보자

접근
1. 입력 받으며 0 나오면 종료
2. 함수 호출
3. 재귀 함수 만들기
def variable_case(start: int, depth: int, case:list) -> None
    # 종료조건 - if depth == 6 then print & return
    
    for i in range(start, len(S)):
        case.append(i)
        get_case(i, depth+1, case)
        case.pop()
4. 
'''
import sys

input = sys.stdin.readline


def get_case(start: int, depth: int, case: list) -> None:
    # 종료 조건
    if depth == 6:
        # case는 int형 리스트기 때문에 str 변환
        print(' '.join(map(str, case)))
        return

    for i in range(start, len(S)):
        if S[i] not in case:
            case.append(S[i])
            get_case(i, depth+1, case)
            case.pop()


while True:
    k, *S = list(map(int, input().split()))

    if k == 0:
        break

    get_case(0, 0, [])
    # case 끝날 때마다 한 줄
    print()
