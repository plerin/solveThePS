'''
>> P
1~N까지 수를 한 번씩 이용해서 가장 긴 증가 부분수열(M)과 가장 긴 감소 부분 수열(K)인 수열을 출력
    - 1~N 수를 한 번식 이용해서 부분 증가 수열길이가 M이고 부분 감소수열길이가 K인 수열을 구하라
>> S
N의 범위를 구하자
    - LIS(Longest Increasing Subsequence) 
    - LDS(Longest Decreasing Subsequence)
    - LIS 와 LDS는 무조건 하나의 수를 공유한다 ==> M + K - 1
    -> N의 범위 M+K-1 <= N <= N * M

접근
    - 1~N개로 M개의 증가 수열과 K개의 감소 수열을 만들어야 해
    1) K개의 수열 만들기 ++ m -= 1 & n -= k
    2) 그 이후부터 n개를 m개로 나눈 개수만큼 부분 수열 만들기
        - m개의 부분 수열만들고 그 안의 원소들은 모두 감소 수열임
        -> [3,2,1] , [5,4], [7,6] -> 각 행의 하나씩 모으면 M, 한 열의 최대 값이 K
코드
    1) 입력 받기
    2) 함수 호출 _ param N, M, K
    3) N 범위 안되는 경우 반환 
    3) K개 원소를 갖는 부분 수열 만들기
    4) while m: 반복하며 n//m개 원소를 갖는 부분수열 만들기
'''


def get_solve(n: int, m: int, k: int) -> str:

    if n < (m + k - 1) or (m * k) < n:
        return '-1'
    else:
        arr = [str(i) for i in range(k, 0, -1)]

        n -= k
        m -= 1

        while m:
            arr.extend([str(i) for i in range(k + (n//m), k, -1)])
            k += (n//m)
            n -= (n//m)
            m -= 1

        return ' '.join(arr)


N, M, K = map(int, input().split())

ans = get_solve(N, M, K)

print(ans)
