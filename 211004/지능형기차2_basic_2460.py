'''
goal : 1~10 정차역이 있는 기차에서 각 역마다 내리고 타는데 그 중 가장 많이 사람있는 경우 반환
1. 변수 선언
    1) ret(list) : 타고 있는 사람 수 누적 _ default 0
1. 입력 받기
    1) 마지막 사람(ret[-1])에 현재 탄사람-내린사람 을 더해서 ret에 추가
2. 결과 반환
    1) max값 반환
'''

# 1
ret = [0]
# 2
for _ in range(10):
    off, on = list(map(int, input().split()))
    ret.append(ret[-1]+on-off)
# 3
print(max(ret))
