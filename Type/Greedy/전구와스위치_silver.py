'''
backjoon url -> https://www.acmicpc.net/problem/2138

>> Keyword
1열로 나열된 전구의 최소한 버튼 누르는 방법
-> left->right _ 어떤 기준으로 버튼 클릭을 판단하느냐(왼쪽 전구 -> 한 칸 지나가면 더이상 변경할 수 없으니까)
이 때 주의사항! 첫번째 전구는 판단기준이 없다 == 이 경우를 대비하여 2가지 경우를 구하고 결과 비교!

>> P
N개 스위치와 전구가 있다.
각 전구는 2가지 상태(켜져 있는상태(0), 꺼져있는 상태(1))를 갖는다.
i번 스위치는 루느면 i-1, i, i+1의 세 개의 전구 상태가 바뀜(처음과 마지막은 2개 전구만 바뀜)
N개 전구를 우리가 만들고자 하는 상태 만들기 위해 최소 몇 번 눌러야 하는가?

>> S
상태 정보가 주어졌을 때 최소 횟수를 구하는 건 최적의 방법을 찾아 진행한다
-> 그리디 알고리즘

접근
1. 최소 횟수를 구해야하므로 버튼 toggle를 최소화 할 방법이 필요하다
-> 왼쪽에서 오른족으로 이동하며 왼족 전구를 기준으로 버튼 클릭여부 판단
(오른쪽으로 진행되다보니 현재 왼쪽에 있는 전구에 맞춰 버튼 눌러가면 최소 횟수 구할수 있어)
2. 첫 번째 전구는 왼쪽 전구가 없다보니 2가지 경우(버튼 누른다/안누른다)모두 구해야함
3. 2번에서 1번 방법으로 구한 값 중 작은 값을 출력

코딩
1. 메소드 2개 선언
- toggle(1<->0) : 버튼 눌렀을 때 전구 상태변화하는 메소드
- search(오른족으로 진행하며 i-1번째 전구를 보며 버튼 누를지 여부 판단)
def toggle(num):
    if num == 1: return 0 else: return 1
def search(blub, cnt):
    ret = 0
    if cnt == 1:
        blub[0] = toggle(blub[0])
        blub[1] = toggle(blub[1])
    for i in range(1, n):
        if blub[i-1] != target[i-1]:
            ret += 1
            blub[i-1] = toggle(blub[i-1])
            blub[i] = toggle(blub[i])
            if i != n-1:
                blub[i+1] = toggle(blub[i+1])

    if blub == target:
        return ret

    return -1
2. 메소드 사용(2번, 버튼 눌렀을 때(1), 안눌렀을 때(0)
3. 2번 결과를 통해 정답 출력

'''
import sys

input = sys.stdin.readline


# 전구 상태 변경 _ 0 <-> 1
def toggle(num: int) -> int:
    return 1 if num == 0 else 0


def search(blub: list, cnt: int) -> int:
    ret = 0
    # cnt == 1이면 첫 번째 전구 버튼 누름
    if cnt == 1:
        ret += 1
        blub[0] = toggle(blub[0])
        blub[1] = toggle(blub[1])
    for i in range(1, N):
        if blub[i-1] != target[i-1]:
            ret += 1
            blub[i-1] = toggle(blub[i-1])
            blub[i] = toggle(blub[i])
            if i != N-1:
                blub[i+1] = toggle(blub[i+1])

    if blub == target:
        return ret

    return -1


N = int(input())
blub = list(map(int, input().rstrip('\n')))
target = list(map(int, input().rstrip('\n')))

# 첫 번째 전구 버튼 누르지 않음(0) / 누름(1)을 구분하여 2번 호출
cnt1 = search(blub[:], 0)
cnt2 = search(blub[:], 1)

print(min(cnt1, cnt2) if min(cnt1, cnt2) > -1 else max(cnt1, cnt2))
