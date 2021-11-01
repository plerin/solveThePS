'''
[P]
주어진 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램 작성

[S]
소수 찾기 == 구현 문제

[L]
1. 조건 살피기
    - 개수(N)는 100이하 수는 1000이하 -> 유클리드로 소수 구해도 됨(범위가 작아서) -> 1000까지 소수를 다 구하고 주어진 수가 소수인지 판별하여 카운트
2. 소수 구하기 로직
    - 준비물 : prime_number(list) 소수인 경우 담기 // visited : 한 번 방문했으면 더 이상 탐색하지마 자원 아까워
    - for i in range(2,1001):
        if i in visited: continue
        prime.append(i)
        for j in range(i,1001,i*i):
            visited.append(j)
3. 주어진 수가 prime에 있는 경우 카운트
    arr = list(map(int, input().split()))
    ret = sum([1 for i in arr if arr in prime])
'''


# def find_prime(max_val):
#     visited = []
#     prime = []

#     for i in range(2, max_val+1):
#         if i in visited:
#             continue
#         prime.append(i)

#         for j in range(i*i, max_val+1, i):
#             visited.append(j)
#     return prime

def find_prime(max_val):
    num = set(range(2, max_val+1))

    for i in range(2, max_val+1):
        if i in num:
            num -= set(range(i*i, max_val+1, i))

    return num


N = int(input())
arr = list(map(int, input().split()))

prime_number = find_prime(1000)

ret = sum([1 for i in arr if i in prime_number])

print(ret)
