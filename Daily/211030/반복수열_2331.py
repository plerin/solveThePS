'''
[P]
D[1] = A
D[N] = D[N-1]의 각 자리 숫자의 P번 곱한 수들의 합
반복 부분 제외하고 수열에 남는 개수를 구하는 프로그램

[S]
DFS로 파고 들다가 값이 이미 방문한 값이면 리턴 
    - 유형 : 그래프 탐색 _ DFS _ 재귀

[L]
1. 입력 받기
    - A(int) : 수열 시작 값 // P(int) : p번씩 곱해(제곱)
2. DFS 함수 호출
3. DFS 함수 선언
    - 목적 : A 값을 규칙에 맞게 구하면서 VISITED에 담고 다음 값이 VISITED에 이미 있는 값이면 개수 반환
    - PARAM : elem(int) : 수열 구성 요소 // visited(list) 기본 값 []
    - logic : 
        1) if elem in visited then return visited  
        2) visited.append(elem) : 방문 체크
        3) sum(map(lambda x: x**2, map(str,visited[-1])) 과 visited를 인자로 재귀호출
    - return : len(visited)(int)
4. 결과 출력
'''


def repeatArr(elem: int, visited: list):
    if elem in visited:
        return len(visited[:visited.index(elem)])

    visited.append(elem)
    next_elem = sum(map(lambda x: int(x)**P, str(visited[-1])))

    return repeatArr(next_elem, visited)


A, P = map(int, input().split())
ret = repeatArr(A, [])

print(ret)
