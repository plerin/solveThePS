'''
> P
1~N인 오름차순 순열이 있는데 바로 이전에 오는 순열을 구하라

이전 순열 <-> 다음 순열
3,1,2 -> 2,3,1 // 바뀔 대상이 첫번째 일 때 3 다음 정순 -> 2 다음 역순
순서는 왼->오, 다음 수(i+1)가 이전 수(i)보다 작은 경우 x,y로 선정
뒤부터 순회(정순이니까 가장 뒷 값이 가장 커)하며 i보다 작은 경우 찍고 스왑
seq[:i] + sorted(seq[i+1:], reverse=True)
'''


def prevPerm(seq: list):
    global N
    x, y = 0, 0
    swap = False

    # 입력된 순열이 가장 앞서는 순열일 경우
    if seq == [i for i in range(1, N+1)]:
        print(-1)
        return

    for i in range(N-1, 0, -1):
        if seq[i-1] > seq[i]:
            x, y = i-1, i

            for j in range(N-1, 0, -1):
                if seq[j] < seq[x]:
                    seq[j], seq[x] = seq[x], seq[j]
                    swap = True
                    break
        if swap == True:
            print(*(seq[:i] + sorted(seq[i:], reverse=True)))
            break


N = int(input())
next_prem = list(map(int, input().split()))

prevPerm(next_prem)
