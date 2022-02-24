'''
목표 : 반대로 읽어도 같은 수인지 판단(str 변환 x)

접근
1. 0보다 작은 경우 처리(false 반환)
2. x를 10으로 나눈 나머지를 누적하며 원래 값과 비교


'''


class Solution:
    def isPalindrome(self, x: int) -> bool:

        origin = x
        conv = 0

        if x < 0:
            return False

        while x:
            r = x % 10
            x //= 10
            conv = conv * 10 + r

        return True if conv == origin else False
