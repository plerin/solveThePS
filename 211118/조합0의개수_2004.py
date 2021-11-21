'''
> P 
이항계수(n,m)의 끝자리 0의 개수를 출력하는 프포그램 작성하시오 
> S
수학
> L
이항계수를 찾는 방식으로 factorial / dp 를 사용하면 메모리/시간 초과 에러가 남 ==> 정수의 범위가 20억이기 때문에
그렇다면 다른 접근이 필요하다는 것
    - 이항계수 식 = n!/(n-m)!*m! 을 사용하고
    - 0의 개수 == 2와 5의 쌍의 개수를 찾으면 됨 
'''

n, m = map(int, input().split())


def countNum(n, m):
    cnt = 0
    while n:
        n //= m
        cnt += n
    return cnt


print(min(countNum(n, 2) - countNum(n-m, 2) - countNum(m, 2),
          countNum(n, 5) - countNum(n-m, 5) - countNum(m, 5)))
