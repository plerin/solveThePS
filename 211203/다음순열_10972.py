'''
> P 
1~N까지 수로 이루어진 수열에서 특정 수열 다음 순열을 구하시오
    - 마지막 값이 주어지면 -1 반환 (예외 경우로 처리)

next-permutation algorithm
1. 역순열을 깨는 경우 찾아라
2. 1번에서 찾은 값보다 바로 위 큰 값을 찾아 스왑한다
3. 재배열한다(스왑 값([:idx] + sorted([idx:])))

func(nextPerm)
    - param : seq(list)
    - vari : global N, x/y(int) _ 이전 값이 현재 값 보다 작은 경우
    - logic
        1) 역순 순회하며 현재 값보다 이전 값이 더 작은 경우 찾기
        2) 스왑하기 

'''


def nextPermulation():
    global N, seq

    x, y = 0, 0
    ret = [-1]
    is_last = True

    for i in range(N-1, 0, -1):
        if seq[i-1] < seq[i]:
            x, y = i-1, i
            for j in range(N-1, 0, -1):
                if seq[j] > seq[x]:
                    seq[x], seq[j] = seq[j], seq[x]
                    is_last = False
                    break
            if is_last == False:
                ret = seq[:y] + sorted(seq[y:])  # 스왑된 후에는 정배열
                break
    return ret


N = int(input())
seq = list(map(int, input().split()))


ans = nextPermulation()

print(*ans)
