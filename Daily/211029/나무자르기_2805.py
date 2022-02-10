'''
[P]
나무 N개 중에서 나무 M미터가 필요하다. 적어도 M미터를 위해 절단기에 설정할 수 있는 높이 최댓값
    - N 범위 : 1~1백만 // M 범위 : 1~20억
[S]
파라메트릭 서치 유형 _ 설정 높이의 최댓 값 == 최적화 == 지속 탐색을 하여 최적화(예/아니요) 문제로 풀어간다.
    - 유형 : 이진탐색 _ START/END/MID 사용  떡볶이 문제와 비슷
[L]
1. 입력 받기
    - N(int) : 나무 개수 // M(int) : 필요 나무 길이
    - trees(list) : 나무 리스트
2. 이진 탐색 준비물
    - start(int) : 0 // end(int) : max(trees) : 나무 길이 중 최댓 값
3. 함수 호출
    - 목적 : 이진탐색을 통해 최적 높이(최댓 값) 리턴
    - PARAM : target(int) : 필요 나무 길이(M) // start(int) : 탐색 시작 값 // end(int) : 탐색 끝 값 
    - logic :
        1) while start <= end  -> mid 구하기 -> 나무 자를 수 있는 양 확인(total) -> 탐색 범위 좁히고 만약 target보다 많은 양이면 max_hei 에 저장
    - return : 나무 최대 높이
4. 결과 출력
'''


def cutting_tree(target, start, end):
    max_hei = 0
    while start <= end:
        total = 0

        mid = (start+end) // 2

        for t in trees:
            if t > mid:
                total += t-mid

        if total < target:
            end = mid-1
        else:
            max_hei = mid
            start = mid+1

    return max_hei


N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

ret = cutting_tree(M, start, end)

print(ret)
