'''
[P]
참가자(P)가 자리(M)에 앉을 때 지정된 좌석에만 앉을 수 있다 못 앉는 참가자 구하라
    - 참가자가 예약한 좌석에 못 앉는 경우
[S]
구현문제
[L]
1. 총 좌석(M)과 예약한 좌석(중복제거) 차를 구하기
    - 참가자가 예약한 좌석을 SET에 넣고 LEN()로 중복제거 한 좌석 구하기
'''

for _ in range(int(input())):
    p, m = map(int, input().split())
    reserve_seat = set([int(input()) for _ in range(p)])
    print(abs(p-len(reserve_seat)))
