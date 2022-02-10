'''
> P
2진수가 주어졌을 때 8진수로 변환하여 출력


2진수 : 0b  _ bin()
8진수 : 0o  _ oct()
16진수 : 0x _ hex()

진수 변환(n진수 -> 10진수)
int(값, [해당 진수])
ex) int(ob1111, 2) -> 15 출력



'''

s = input()

print(oct(int(s, 2))[2:])


# ten_number = 0
# answer = ''
# for i in range(len(x)):
#     tem_number += int(x[-1])*(2**i)
#     x = x[-1]

# for i in range(len(x)):
#     tot += x[len(x)-i-1] * (2**i)
