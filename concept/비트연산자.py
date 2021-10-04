'''
비트 연산자를 활용해 멋있게 코딩 가능하다. (멋있다는 건 중요한 것)
'''

# 3. 2진수에서 1 비트 개수 구하기


def count_bit(n):
    return n % 2 + count_bit(n//2) if n >= 2 else n


def bit_count(n):
    k = 0
    count = 0

    while n >= (1 << k):
        if n & (1 << k) != 0:
            count += 1
        k += 1

    return count


print('1000은 2진수로 ', bin(1000), '이고, 1의 개수는', bit_count(1000), '개입니다')

# True/False Toggle

onOff = True
onOff = False if onOff else True
print(onOff)
onOff = False if onOff else True
print(onOff)

onOff = True
onOff ^= True
print(onOff)
onOff ^= True
print(onOff)
