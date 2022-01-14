'''
>> P
N명의 여학생과 M명의 남학생이 팀원을 찾고 있다.
인원 중 K명은 인턴쉽에 참여해야하고 대회 참가랑 중복될 수 없다.
최대 팀 수를 구하라
    - 1팀 = 여 2 + 남 1
>> S
남여 비율대로 줄어들고 남은 수를 K에서 차감
ex) N, M, K가 6 3 2리면
    6 3 2 -> 
    4 2 2 -> 1팀 
    2 1 2 -> 2팀  --> 그만 조건은 N+M >= 5 and N >= 2

>> C
1. 입력 받는다
N, M, K = map(int, input().split())

2. N+M >= 5 and N >= 2:
    ret += 1
    N -= 2
    M -= 1
'''

N, M, K = map(int, input().split())
ans = 0

while N+M >= K and N >= 2 and M >= 1:
    N -= 2
    M -= 1
    ans += 1

print(ans if N+M >= K else ans - 1)  # 그룹을 다 지은 뒤 남은 인원이 K명보다 적을 경우 한 그룹 해체
