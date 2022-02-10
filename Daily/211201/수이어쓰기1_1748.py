'''
> P
1부터 N까지 수를 이어 쓸 때 자릿 수를 구하라
    - N 제한값이 1억 & 시간제한 1초 미만 -> O(N)도 불가능
> S
나누기 나머지를 활용.
1의 자리    -> 개수 * 1
10의 자리   -> 개수 * 2
100의 자리  -> 개수 * 3 
각 자리의 수가 몇 개인지 알아내기
    -> 25 = 1의자리 9개(1~9), 10의자리 16개(10~25)
        %10 = 2..5 , %10 0..2
    -> 153 = 1의 자리 9개(1~9), 10의자리 90개(10~99), 100의자리 54개(100~153)

10-1, 10**2-10, 10**3-100

while n 
-> n - 10**i-10**(i-1)

input : n(int)
vari : ans(int)=0
logic
    1) while n - 9*(10**i) => i start with 0
    2) ans += 9*(10**i) * (i+1)
    3) else ans += n*(i+1)
    4) return 

rule
    1. 입력 값의 자리 수에 따른 값을 구한다
        if n > 9 then add 9 * 1(1의 자리 개수)
        if n-result1 > 90 then add 90 * 2(2의 자리 숫자 개수)
        else 현재 남은 수 * 자리 수(i+1)

개선안
입력 값의 자리 수를 구하고 
n-1 까지의 자리 수 합 + n 자리의 자리수 합

~ n-1
while i < n_len:
    ans += 9 * (10*i) * (i+1)
    i += 1
n
ans += ((int(n) - (10**n_len)) + 1) * (n_len+1)
'''


# def continueNum(n: int):
#     ans = 0
#     i = 0

#     while n > 9*(10**i):
#         n -= 9*(10**i)
#         ans += 9*(10**i) * (i+1)
#         i += 1

#     ans += n * (i+1)

#     return ans

def continueNumImprove(n: int):
    ans, i = 0, 0
    len_n = len(str(n))-1

    while i < len_n:
        ans += 9 * (10**i) * (i+1)
        i += 1

    ans += ((n - (10**len_n))+1) * (len_n+1)

    return ans


N = int(input())

ret = continueNumImprove(N)

print(ret)
