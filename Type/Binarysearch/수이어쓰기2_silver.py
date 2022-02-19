'''
backjoon url -> https://www.acmicpc.net/problem/1790

>> Keyword
범위가 1억이상 => 이진탐색 or 규칙을 통해 빠른 계산법이 있을거라 예상
패턴 = 자리수에 따라 9*1, 90*2, 900*3 순으로 길어진다(누적하며 진행)

1. k가 속한 자리수를 구한다
    k가 9*10**(자리수-1) * 자리수 보다 클 경우 반복하며 ans값 누적
2. k번째 값이 있는 수를 구한다
    ans = (ans+1) + (k-1) // digit -> k가 속한 수를 구하기
3. n과 비교하고 k번째 값을 반환 
    if ans > n then print(-1) else print(str(ans)[(k-1)%digit])

>> P
1부터 N까지 수를 이어서 쓰면 새로운 수를 얻는다.
앞에서 K번째 숫자가 어떤 숫자인지 구하라
    - 범위 -> N ~ 1억 // k ~ 10억
    - 수의 길이가 k보다 작아서 자리 숫자가 없는 경우 -1 출력
>> S
범위가 큰 경우 이진탐색과 같은 풀이 사용해야함 
수의 길이와 k간 비교가 필요 -> k번째 수가 어떤 수인지 알아야 함

접근
1. N이 몇번째 자리수인지에 따라 길이가 달라짐
자리수      갯수
1자리 -> 9 * 1
2자리 -> 10~99 = 90 * 2개
3자리 -> 100~999 = 900 * 3 개
=> n자리 -> 9 * 10**(자리수-1) * 자리수 규칙을 따름

2. 위와 같은 접근으로 k가 어떤 수에 속한 값인지 찾기
3. 해당 수에서 인덱스로 접근

코딩
1. 필요 변수 선언 
num = 0 # k번 값을 갖는 수
digit = 1 # 자리수

2. 자리수 구하기
while k > 9 * 10**(digit-1) * digit:
    k -= 9 * 10**(digit-1) * digit
    num += 9 * 10**(digit-1)
    digit += 1
3. num 구하기
num = (num+1) + (k-1) // digit

4. num과 n 비교 및 결과 표출
if n > num:
    print(-1)
else:
    print(str(num)[(k-1)%digit])
'''

n, k = map(int, input().split())

# num = k번째 값을 갖는 수, digit = 자리수
num = 0
digit = 1

# 자리수를 구함
while k > 9 * 10**(digit-1) * digit:
    k -= 9 * 10**(digit-1) * digit
    num += 9 * 10**(digit-1)
    digit += 1

# num은 9,99,999이므로 1을 더해서 10의 배수로 맞추고 k에서 1을 뺀뒤(num으로 준값) digit을 나눠 해당 자리수에 몇번째 값인지 구함
num = (num+1) + (k-1) // digit


if n < num:
    print(-1)
else:
    # num을 str 변환 후 (k-1)를 digit으로 나눈 나머지 값을 통해 k번째 출력!
    print(str(num)[(k-1) % digit])
