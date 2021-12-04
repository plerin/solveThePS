'''
> P
1~N까지 수로 이루어진 오름차순 순열이 있다 다음에 오는 순열을 구하시오

오름차순 순열은 
3,4,2,1 -> 4,1,2,3
맨 앞자리를 기준으로 보면 3 + 역순 -> 4(3보다 바로 큰 수) + 정순

1. 뒤에서 앞으로 탐색하며 (i-1)이 i번째 값보다 작은 경우 찾아 저장하기
    -> for i in range(n-1,0,-1) 
    -> if seq[i-1] < seq[i] then x = i-1, y = i
2. i-1 수와 그 바로 윗 수와 스왑
    -> for j in range(n-1, 0, -1):
    -> if seq[j] > seq[x] then seq[x], seq[j] = seq[j], seq[x] and swap = True and break
3. 재정렬 한 값 반환(다음 순열)
    -> if swap = True then print(seq[:y] + sorted(seq[y:]))
'''


def nextPerm(prev: list):
    global N
    x, y = 0, 0
    swap = False

    if prev == [i for i in range(1, N+1)][::-1]:
        print(-1)
        return

    for i in range(N-1, 0, -1):
        if prev[i-1] < prev[i]:
            x, y = i-1, i

            for j in range(N-1, 0, -1):
                if prev[j] > prev[x]:
                    prev[x], prev[j] = prev[j], prev[x]
                    swap = True
                    break

        if swap == True:
            print(*(prev[:y] + sorted(prev[y:])))
            break


N = int(input())
prev_perm = list(map(int, input().split()))

nextPerm(prev_perm)
