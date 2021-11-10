'''
[P]
00시 00분 00초부터 N시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수 출력
[S]
구현(implementation) 문제로 모든 경우의 수를 구하면 됨
    - 완전 탐색(Brust forcing) : 가능한 경우의 수 모두를 검사하는 탐색 _ 모든 경우의 수가 처리할 수 있다면 이 방법으로 실행 가능 
[L]
1. 입력 받기
    - N(int) _ N시 59분 59초 의미하는 숫자
2. 하루를 초로 환산하면 86400초 -> for문으로 반복하며 '3'이 있으면 cnt+1
    1) ret(int) _ 결과 값 담을 변수 선언
    2) 시/분/초 3중 for문 실행 _ 시(hour)는 입력받은 N+1을 입력,
    3) 시/분/초를 문자열로 합치고 '3' 여부 확인('3' in) _ 있다면 ret +=1
3. 결과 리턴
'''

N = int(input())

ret = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                ret += 1

print(ret)
