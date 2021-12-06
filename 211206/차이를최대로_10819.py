'''
> P
N개의 정수로 이루어진 배열 a에서 최댓 값을 구하는 프로그램 작성

1. 순열의 모든 값을 구하면서 해당 순열에서 가장 큰 값을 저장
    - 순열 값 구하는 방법
        1) 라이브러리 이용(permutations)
        2) 다음 순열 알고리즘 사용
            - reverse 탐색 (n-1,0,-1) -> if [i-1] < [i] then x, y = i-1, i
            - 재 탐색 [x] < [j] 큰 값 과 스왑 후 break 
            - seq 갱신 후 sum구하기
2. 순열의 합을 구하는 로직
sum([abs(seq[i] - seq[i+1]) for i in range(len(seq)-1)])
'''


def maximumVal():
    global ans, arr
    x, y = 0, 0

    arr.sort()
    while arr != sorted(arr, reverse=True):
        swap = False
        for i in range(N-1, 0, -1):
            if arr[i-1] < arr[i]:
                x, y = i-1, i

                for j in range(N-1, 0, -1):
                    if arr[x] < arr[j]:
                        arr[x], arr[j] = arr[j], arr[x]
                        swap = True
                        break
            if swap == True:
                arr = arr[:y] + sorted(arr[y:])
                ans = max(ans, sum([abs(arr[i] - arr[i+1])
                                    for i in range(len(arr)-1)]))
                break
        print(arr)


N = int(input())
arr = list(map(int, input().split()))
ans = 0

maximumVal()

print(ans)
