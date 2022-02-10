'''
>> P
양수 N의 숫자를 조합해서 30배수가 되는 가장 큰 수를 만들어라
    - 존재하면 수 출력 존재하지 않으면 -1 출력
>> S
조합의 모든 경우의 수 중 30의 배수를 찾는 게 아니라 
가장 숫자가 큰 경우가 30의 배수인지 찾는 문제

가장 큰 조합
    - 역정렬
30의 배수
    - 모든 수의 합이 3에 나누어 떨어지는지(% 3 == 0)
    - 0이 있는지(맨 마지막 숫자가 0이어야 함)

>> C
arr = list(input())
arr.sort(reverse=True)
sumv = 0
if '0' not in arr:
    print(-1)
else:
    for i in arr:
        sumv += int(i)
    if sumv % 3 == 0:
        print(''.join(arr))
    else:
        print(-1)

>> 소감
이 문제는 풀이는 간단한데 이해가 어려웠어
처음 접근을 당연히 조합 중 30의 배수가 되는 경우로 생각함(가장 큰 조합이 30배 수가 아니면 그보다 작은 조합이 30배수인지..)
    - 이런 접근은 문제 제한 조건에 막혀 숫자가 10**5개인 경우니까 제한에 통과할 수 없어
접근 방법이 가장 큰 조합(sort(reverse=True)) 이후에도 30의 배수의 조건
    - 10의 배수 & 3의 배수
        -> 10의 배수는 마지막 수에 0이 있는가?
        -> 3의 배수는 모든 구성 수의 합을 3으로 나눈 나머지가 0인지!


'''

arr = list(input())
arr.sort(reverse=True)
sumv = 0

if '0' not in arr:
    print(-1)
else:
    for i in arr:
        sumv += int(i)
    if sumv % 3 == 0:
        print(''.join(arr))
    else:
        print(-1)
