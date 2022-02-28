'''
backjoon url -> https://www.acmicpc.net/problem/2343

>> Keyword
이분탐색(파라메트릭 유형) 
무엇을 탐색할 것인지가 가장 중요!
-> 블루레이의 최소 크기

블루레이 개수와 크기의 상관관계를 이분탐색으로 풀었어
s = 레슨 중 제일 큰 값, e = 레슨들의 합
    -> 레코드 개수가 부족하면 right = mid - 1, 블루레이 크기 줄여
    -> 레코드 개수가 넘어가면 left = mid + 1, 블루레이 크기 늘려

>> P
N개의 강의를 M개 블루레이에 저장하려고한다
    - 강의 순서가 바뀌며 안됨 (i~j 강의를 녹화하려면 i와 j 사이 모든 강의도 같은 블루레이에 녹화)
    - 블루레이는 모두 같은 크기를 가져야하고 최소 값 구하기

>> S
데이터를 정렬한 뒤 최적해를 구하는 파라메트릭 서치 유형인 것 같아.
로직을 수행할 때 기준이 되는 값이 무엇인지가 중요,
17은 15보다 크기 때문에 다시 호출? 기준은?

과정
1. 입력 받음
2. left, right 구함
3. 이분탐색 반복
    - 레코드 크기 중간값 구함(mid)
    - 현재 레코드 크기에서 필요로 한 레코드 개수 구하기
        - 레코드 개수가 많다(cnt > M) -> left = mid + 1(크기를 늘린다)
        - 레코드 개수가 부족(cnt <= M) -> right = mid -1(크기를 줄인다)        
'''


def add_lesson():
    cnt = 0  # 레코드 갯수 세기
    sum_lesson = 0  # 한 레코드에 들어갈 레슨들의 합

    for i in range(n):
        if sum_lesson + lesson_list[i] > mid:
            cnt += 1
            sum_lesson = 0

        sum_lesson += lesson_list[i]
    else:
        if sum_lesson:
            cnt += 1
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    lesson_list = list(map(int, input().split()))

    right = sum(lesson_list)  # 레코드 가장 큰 값 = 모든 레슨 담을 수 있는 값
    left = max(lesson_list)  # 레코그 가장 작은 값 = 레슨 중 가장 큰 값을 담을 수 있는 값

    while left <= right:
        mid = (left + right) // 2
        cnt = add_lesson()  # 현재 레코드 크기에서 넣을 수 있는 레슨 수
        if cnt <= m:        # 레코드 숫자가 모자라면 레코드 크기(mid)를 줄인다
            right = mid - 1
        elif cnt > m:       # 레코드 숫자가 많아지만 레코드 크기(mid)를 키운다
            left = mid + 1

    # 답은 left = 최소 크기
    print(left)
