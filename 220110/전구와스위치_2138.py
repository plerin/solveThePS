'''
>> P
N개의 스위치와 전구가 있을 때 원하는 상태로 만들기 위해 필요한 최소 횟수 구하라
    - 상태는 2가지 : 0 (켜짐) / 1 (꺼짐) 만 존재
    - i 스위치 누르면 i-1 / i / i+1 이 toggle (양 끝은 2개만)
>> S
상황에 따른 최소 횟수 & 현재 상태에 따라 toggle => 그리디 알고리즘
a와 b가 있을 때 1,2번을 반복
1. a와 b가 다른 위치를 찾는다.
2. 해당 위치에서 toggle 
3. a가 변화하다가
    - 처음 a로 돌아온 경우 -> -1 반환
    - b가 된 경우 -> 횟수 반환

프로세스
1. 입력 받음 _ bulb_a, bulb_b
2. 함수 호출
def solve():
    global bulb_a
    ret = -1
    cnt = 0
    origin = bulb_a
    while True:
        pos = 0
        # 다른 위치 찾기
        for i in range(N):
            if bulb_a[i] != bulb_b[i]:
                pos = i
                break
        # 바꾸기
        if pos == 0:
            for i in range(pos, pos+2):
                bulb_a[i] = 1 - bulb_a[i]
        elif pos == N-1:
            for i in range(pos-1, pos+1):
                bulb_a[i] = 1 - bulb_a[i]
        else:
            for i in range(pos-1, pos+2):
                bulb_a[i] = 1 - bulb_a[i]

        # 확인_origin/b
        if bulb_a == origin:
            break
        elif bulb_a == bulb_b:
            ret = cnt
            break
        
    return ret
3. 결과 출력
'''


def solve():
    global bulb_a

    ret, cnt = -1, 0
    origin = bulb_a[::]

    while True:
        pos = 0
        cnt += 1
        for i in range(N):
            if bulb_a[i] != bulb_b[i]:
                pos = i
                break

        if pos == 0:
            for i in range(pos, pos+2):
                bulb_a[i] = 1 - bulb_a[i]
        elif pos == N-1:
            for i in range(pos-1, pos+1):
                bulb_a[i] = 1 - bulb_a[i]
        else:
            for i in range(pos-1, pos+2):
                bulb_a[i] = 1 - bulb_a[i]
        print(bulb_a)
        # 확인_origin/b
        if bulb_a == origin:
            break
        elif bulb_a == bulb_b:
            ret = cnt
            break

    return ret


N = int(input())
bulb_a = list(map(int, input()))
bulb_b = list(map(int, input()))

ans = solve()

print(ans)
