'''
goal : 주어진 일자 중 일의 자리 숫자와 차량이 같은 수를 반환
1. 입력 받기 _ 일자를 받는데 %10으로 일의자리수를 저장해두기
2. 입력된 차량 번호 중 같은 것 카운트해서 결과 출력 
'''
day = int(input()) % 10
print(len(list(filter(lambda x: int(x) == day, input().split()))))
