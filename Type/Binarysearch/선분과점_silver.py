'''
backjoon url -> https://www.acmicpc.net/problem/11664

>> Keyword
파라매트릭 서치(중간점에서 거리를 구하며 최적화문제로 판단),
3차원 배열을 다룰 수 있는가?
- 두 점의 중간 구하기 = (ax+bx)/2, (ay+by)/2, (az+bz)/2
- 거리 최솟값 오차 범위 10**(-6)까지 허용
    -> if abs(ans-h) < 1e-6 
- a,b와 c까지 거리를 통해 갱신
    -> if l < r else  -> x,y,z 갱신

>> P
3차원 좌표 위 1개 선분과 1개 점이 있을 때 
선분과 점 사이의 거리 최솟값 구하라
    - 거리 공식 = sqrt{(x2-x1)^2+(y2-y1)^2+(z2-z1)^2} 이다.
    - 절대/상대 오차는 10**(-6)까지 허용
>> S
파라메트릭 서치로 구할 수 있겠다 어떻게?
    - 선분과 점의 최소 거리 = 직각이 되는 지점 = 선분의 중간지점과 거리를 구하고 가까운 곳으로 이동! = 최적해 구하기

접근
1. a와 b 사이 중간점 m을 구한다
2. a, b, m 각 점마다 c와의 거리를 계산
3. h가 현재 최소값인 ans보다 작으면 ans를 h로 갱신
4. l이 r보다 크면 c가 a보다 b에 가깝다는 의미로 a를 m으로 갱신 
5. r이 l보다 크면 c가 b보다 a에 가깝다는 의미로 더 멀리있는 b를 m으로 갱신
6. 위 작업 반복하다 ans와 h의 차가 오차범위 안으로 들어오면 정답 출력 후 종료

'''

# a,b,c 각 좌표(x,y,z)를 입력 받음
ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

# 최소값 저장위한 변수 선언
ans = float('inf')

while True:
    # 중간 지점 구함
    mx, my, mz = (ax+bx)/2, (ay+by)/2, (az+bz)/2

    # a,b,m에서의 c까지 거리 구함
    l = ((ax-cx)**2+(ay-cy)**2+(az-cz)**2)**0.5
    m = ((mx-cx)**2+(my-cy)**2+(mz-cz)**2)**0.5
    r = ((bx-cx)**2+(by-cy)**2+(bz-cz)**2)**0.5

    # ans와 m(중간점에서 c까지 거리)의 차가 오차범위 이내인 경우
    if abs(ans-m) < 1e-6:
        print('%0.10f' % ans)
        break
    if m < ans:
        ans = m
    # atoc 거리가 btoc보다 짧음 == a가 b보다 c와 가깝다 == b를 현재 중간(m)으로 갱신
    if l < r:
        bx, by, bz = mx, my, mz
    else:
        ax, ay, az = mx, my, mz
