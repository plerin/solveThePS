'''
>> P
N개 단어가 주어지는데 단어는 알파벳 대문자로 이루어져 있다.
각 알파벳을 0~9숫자 중 하나로 바꿔 N개의 수를 합하여 최대를 만드는 프로그램 작성
    - 각 알파벳은 유일한 숫자를 지정받는다.
>> S
단어의 길이가 같을 때와 아닐 때를 구분
    - 단어 길이의 차 만큼 그 단어는 가장 큰 값을 지정

1. 대문자 알파벳 리스트를 만들고 그 값은 -1로 초기화 
    -> ord('A')  / chr(65) 를 이용
2. 단어 별 자리 수를 갱신해줘
    -> ACDEB / GCF가 있을 때
    -> 5= A, 4 = C, 3 = D,G, 2= C,E 1 : B,F
'''
import heapq

visited = [False] * 26  # A~Z

# a = [(1, 2), (2, 3)]

a = []

heapq.heappush(a, (1, 'A'))
heapq.heappush(a, (3, 'B'))
heapq.heappush(a, (3, 'S'))
heapq.heappush(a, (5, 'D'))

print(heapq.)
