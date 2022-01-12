'''
>> P
수열 A가 주어졌을 때 가장 긴 증가 부분 수열을 구하라
    - 크기가 100만 값의 범위가 100만 == 크다
>> S
가장 긴 == 최대 값을 구하라 & 범위가 커 == 효율적으로 구하라
    -> 그리디 써볼까?
전구와 스위치 문제로 치환하면 1차원으로 나열된 배열에서 최고 효율을 뽑으려면 왼쪽 / 오른쪽 탐색하며 이전꺼는 다시 확인 하지 않는 것
    - 전구문제 : 왼쪽 값을 보고 판단했어 toggle 여부를
    - 수열문제 : 계속 커져야해 
        1) idx=0부터 시작
        2) 뒷자리(i+1)가 i보다 작거나 같으면 새로 시작하며 카운트 저장 & 출발 값 갱신(현재까지 누적)
        3) 뒷자리(i+1)가 i보다 크면 cnt + 1
>> C
1. 입력 값 변수 저장
N = int(input())
seq = list(input().split())
# ans = -1e9
2. 함수 호출 _ 로직
ans = solve()
def solve():
    ret = -1e9
    
    prev = seq[0]
    cnt = 0
    for i in range(len(seq)-1):
        if prev < seq[i+1]:
            cnt += 1
        else:
            ret = max(ret, cnt)
            cnt = 0
            prev = seq[i+1]
    
    return ret
'''


def solve() -> int:
    ret = 0

    prev = seq[0]
    for i in range(len(seq)-1):
        if prev < seq[i]:


N = int(input())
seq = list(input().split())

ans = solve()

print(ans)
