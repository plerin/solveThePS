'''
>> P
N개의 전구가 있고 2가지 상태(꺼짐/켜짐)를 갖고있을 때
A상태가 B상태가 되도록 하기 위해 toggle해야 하는 최소 횟수를 구하라
    - 상태 : 0(켜짐) / 1(꺼짐)
    - toggle : i -> i-1 / i / i+1 (단, 첫번째와 마지막은 2개만 변경)
>> S
1. 최소 횟수를 구해야하므로 앞뒤 이동이 아니라 한 방향(왼쪽/오른쪽)으로만 진행
    - 판단 기준 : 왼쪽 전구가 같은지 -> 같다면 continue 다르다면 toggle
2. 첫번째 전구는 왼쪽 전구가 없으므로 모두 구해야함(toggle한경우 / 안 한 경우)
    - 1번 반복을 2회 실시

>> C
1. 입력 값 받기
n = int(input())
now = list(map(int, input()))
target = list(map(int, input()))
2. 결과 구하는 함수 호출
ans = solve()
def solve() -> int:
    ret = -1

    for i in range(2):
        case = now[:]
        cnt = 0

        for j in range(len(case)):
            if j == 0 and i == 0:
                pass
            elif 0 < j < N-1:
                pass
            elif j == N-1:
                pass
        
        if case == target:
            ret = cnt
            break
    
    return ret
3. 2번 결과값을 출력
print(ans)
'''


def solve() -> int:
    ret = 1e9

    for i in range(2):  # 첫번째 전구경우(toggle/not toggle)구하기 위해
        case = now[:]   # 본래 상태 값 입력
        cnt = 0
        # print(case)
        for j in range(len(case)):
            if j == 0 and i == 0:   # i == 0(첫 전구 toggle한 경우)
                case[0] = 1 - case[0]
                case[1] = 1 - case[1]
                cnt += 1
            elif 0 < j < len(case)-1:
                if case[j-1] != target[j-1]:
                    case[j-1] = 1 - case[j-1]
                    case[j] = 1 - case[j]
                    case[j+1] = 1 - case[j+1]
                    cnt += 1
            elif j == len(case)-1:
                if case[j-1] != target[j-1]:
                    case[j-1] = 1 - case[j-1]
                    case[j] = 1 - case[j]
                    cnt += 1

        if case == target:
            ret = min(ret, cnt)

    return ret if ret != 1e9 else -1


# 입력 받기
n = int(input())
now = list(map(int, input()))
target = list(map(int, input()))

# 로직 함수 호출
ans = solve()

print(ans)
