'''
goal : 수 10개를 입력 받은 뒤 각 수에 42를 나눈 나머지 중 서로 다른 나머지가 몇 개인지 출력
0. 라이브러리 추가 : 없음
1. 입력 받기
    0) ret(set) 선언
    1) 10개의 수를 입력 받으며 %42 한 값을 ret에 입력
2. 결과 출력
    1) len(ret) 출력
'''

#1
ret = set()
for _ in range(10):
    ret.add(int(input())%42)
#2
print(len(ret))