'''
a,b,c 값이 주어졌을 때 각 연산의 결과를 띄어쓰기로 구분하여 작성
'''

A, B, C = list(map(int, input().split()))

print((A+B) % C)
print(((A % C)+(B % C)) % C)
print((A*B) % C)
print(((A % C)*(B % C)) % C)
