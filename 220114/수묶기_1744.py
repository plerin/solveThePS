'''
>> P
길이가 N인 수열이 주어지고 두 수를 묶는 경우와 묶지 않는 경우가 있을 때
적절히 묶어 합이 최대가 되는 경우를 구하라
    - 연산 : 묶인 수는 서로 곱한 뒤 더한다.
    - 제한 : 묶는 경우는 최소 0번 최대 1번
>> S
최선의 경우를 따져 연산하라.
    - '+' 인경우 -> 두 수를 더한 값과 곱한 값을 비교하여 진행
    - '-' 인 경우 -> 짝수로 곱하고 나머지는 0이 있는 경우만 곱해
    - 큰 수끼리 묶어 + '-'인 경우는 0이 아니면 묶지마 + 
>> C
1. 0보다 큰 경우와 0보다 작거나 같은 경우 2가지로 나눠(리스트)
N = int(input())
plus, minus = [], []
for _ in range(N):
    num = int(input())
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)
2. 정렬(0보다 크면 오름차순 - 작거나 같으면 내림차순)
plus.sort()
minus.sort(reverse=True)

3. while-pop()하며 값을 더해줘
    - 0보다 큰 경우 판단 기준 > 곱한 게 큰지 더한게 큰지 

tmp = []
while plus:
    tmp.append(plus.pop())
    if len(tmp) == 2:
        sum_val, mul_val = tmp[0]+tmp[1], tmp[0]*tmp[1]
        ret = ret + sum_val if sum_val > mul_val else ret + mul_val
        tmp = []
ret += sum(tmp)

while minus:
    tmp.append(minus.pop())
    if len(tmp) == 2:
        ret += tmp[0]*tmp[1]
ret += sum(tmp)

'''


def solve() -> int:
    global plus, minus
    ret = 0

    # 2칸씩 넘어가며 다음칸이 마지막인 경우만 처리
    for i in range(0, len(plus), 2):
        if i == len(plus) - 1:  # 반복 후 남는 한자리 값을 더해줌
            ret += plus[i]
            break
        # 1과 같이 연산될 경우 더한 값이 곱한 값보다 큼
        ret += max(plus[i]+plus[i+1], plus[i]*plus[i+1])

    # 작은 수부터 처리 -> 연산은 plus와 동일
    for i in range(0, len(minus), 2):
        if i == len(minus) - 1:
            ret += minus[i]
            break

        ret += minus[i]*minus[i+1]  # '-'연산 특성상 더하기 처리해줄 필요 없음

    return ret


N = int(input())
plus, minus = [], []

for _ in range(N):
    num = int(input())
    if num > 0:
        plus.append(num)
    else:   # 0도 minus으로 분류
        minus.append(num)

# plus는 큰 수부터 처리, minus는 작은 수부터 처리하기 위한 정렬
plus.sort(reverse=True)
minus.sort()

ans = solve()

print(ans)
