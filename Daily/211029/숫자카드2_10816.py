'''
[P]
상근이는 숫자 카드 N개를 갖고있다. 정수 M개가 주어졌을 때 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하라
    - 범위가 N,M 모두 1~50만, 값의 범위는 -1천만~1천만
[S]
탐색을 해야하는데 선형탐색(O(N**2))하면 시간초과 => 이진탐색으로 풀어보자
    - 유형 : 이진탐색 _ 선 정렬 필요 _ 문제 키워드 : 값 범위 엄청 클 때 / 정렬 / 탐색 / O(logN)
[L]
1. 입력 받기
    - N(int) : 숫자 카드 개수 , cards(list) : 숫자 카드 리스트
    - M(int) : 정수, m_arr(list) : 정수 리스트
2. 이진 탐색 준비물 
    - 라이브러리 : bisect_left, bisect_right 
    - 정렬 : cards.sort()
3. m_arr 반복하며 이진탐색 개수 구하는 함수 호출
    _ 목적 : cards(list)에서 해당하는 정수(x)가 몇개 있는지 개수 리턴
    - param : x(int) 탐색할 정수
    - return : cards에서 x 개수
4. 결과 출력
'''

from bisect import bisect_left, bisect_right


def binary_search(e):
    right_idx = bisect_right(cards, e)
    left_idx = bisect_left(cards, e)
    return right_idx - left_idx


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))

cards.sort()

ret = []
for e in m_arr:
    ret.append(binary_search(e))

print(*ret)
