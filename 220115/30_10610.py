'''
>> P
양수 N을 입력받았을 때 포함된 숫자들을 섞어 가장 큰 30 배수를 구하라
    - 0으로 시작하지 않는다.
    - 존재하지 않으면 -1 출력
>> S
숫자들의 조합으로 가장 큰 30 배수 만들기
탐욕법으로 생각하면 가장 큰 경우를 만드는 경우를 찾아 적용해보기 
    - 모든 자리를 다 사용하는 경우
    - 큰 숫자가 앞에 나오는 경우
naive한 방법으론 
len()만큼 permutations 만들고 


'''

from itertools import permutations

n = list(input())
n.sort(reverse=True)

sum = 0
for i in n:
    sum += int(i)
print(n)
if sum % 3 != 0 or "0" not in n:    # 숫자를 더한 값을 3으로 나눈 나머지가 0이 아니거나 n에 0이 없는 경우
    print(-1)
else:
    print(''.join(n))
