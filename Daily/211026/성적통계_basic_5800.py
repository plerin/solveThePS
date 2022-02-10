'''
[P]
각 반의 학생들의 수학 성적을 지정 문자열 포맷에 맞게 최대 점수,최소 점수, 점수 차이를 출력하라
    - 점수 차이 : 내림차순 정렬했을 때 가장 큰 인접한 점수 차이

[S]
구현(implementation)문제 
    - 정렬 후 인접한 큰 수 차이를 어떻게 구할까? _ len()-1 만큼 반복하며 n과 n+1 차이를 max에 계속 비교해 담아
[L]
1. 함수 이용
    - PARAM : class(int) : 반 / scores(list) : 각 반의 수학 점수 리스트
    - LOGIC :
        1) max = 0 선언
        2) len(scores)-1만큼 반복 -> score[i]와 score[i+1] 차를 max 값으로 갱신
        3) 결과 출력 
'''


def statistics(clas, lst):
    n, *scores = lst
    diff = 0

    scores.sort(reverse=True)

    for i in range(len(scores)-1):
        diff = max(diff, scores[i] - scores[i+1])

    print(f'Class {clas}')
    print('Max {0}, Min {1}, Largest gap {2}'.format(
        max(scores), min(scores), diff))


for i in range(1, int(input())+1):
    statistics(i, list(map(int, input().split())))
