'''
[P]
N개의 공장에서 라면을 사는데 필요한 최소 금액 출력
    - 라면을 사는 경우가 3개 있어
    - i번 공장 : 3원/1개
    - i번 공장 + (i+1)번 공장 : 5원/1개
    - i번 공장 + (i+1)번 공장 + (i+2)번 공장 : 7원/1개
[S]
효율적인 구매 방법을 구하자 내가 생각한 것 처럼 간단한 건 아니더라 
접근
    1) 3- > 2 -> 1 순으로 효율적이다. 
        - 반례 : 1121 인 경우 111로 먼저 풀면 7 + 3*2 = `2
    2) 그럼?  x[i+1] 과 x[i+2]를 비교해서 더 큰 경우부터
        1) [i+1] > [i+2] -> 2->3->1 순으로 풀기 
        2) [i+2] > [i+1] -> 3->2->1 순으로 풀기
    유형은 그리디 알고리즘 => 최적의 해를 구하는 방법을 먼저 선택
[L]
1. 입력 받기
    - N(INT) : 라면 공장 수
    - factory(list) : 공장마다 구매 수 
2. 최적해 구하는 경우 셋팅
    - 라면 공장 수만 큼 반복(n-2까지 i+2비교하기 때문)
    - compare with i+1 and i+2
    - if i+1 > i+2 then  2->3->1 순으로 구하기
    - else: 3->2->1 순으로 구하기
    - 남은건 *3
4. 결과 출력
'''
# 키포인트 : 3->2->1 맞는데 딱 한 가지 경우 i+1 > i+2 인 경우는 2개씩 구매 먼저 진행


def buyTriple(idx):
    global cost
    k = min(arr[idx:idx+3])
    cost += k*7
    arr[idx] -= k
    arr[idx+1] -= k
    arr[idx+2] -= k


def buyDouble(idx):
    global cost     # 전역변수로 선언한 cost를 각 함수에서 사용
    k = min(arr[idx:idx+2])     # 리스트에서 특정 index에 해당하는 값의 min을 찾는 방법
    cost += k*5
    arr[idx] -= k
    arr[idx+1] -= k


def buyEach(idx):
    global cost
    cost += arr[idx]*3


N = int(input())
arr = list(map(int, input().split())) + [0, 0]
cost = 0

for i in range(N):
    if arr[i+1] > arr[i+2]:
        # 만약 arr[i], arr[i+1]로 하면 이후 triple을 못 할 수 있다. ==> 손실
        k = min(arr[i], arr[i+1]-arr[i+2])
        cost += k*5
        arr[i] -= k
        arr[i+1] -= k

        buyTriple(i)
    else:
        buyTriple(i)
        buyDouble(i)
    buyEach(i)

print(cost)
