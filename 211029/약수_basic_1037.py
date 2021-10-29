'''
규칙을 찾아봤어 진짜 약수만 갖고 배수를 구하는 방법
약수의 개수에 따라 공식이 있던데?
    - 약수 1개 : 제곱
    - 약수 2개이상 : [0]*[-1]
'''

N = int(input())
array = list(map(int, input().split()))

array.sort()

print(array[0]*array[-1])

# if len(array) == 1:
#     print(array[0]**2)
# else:
#     print(array[0]*array[-1])
