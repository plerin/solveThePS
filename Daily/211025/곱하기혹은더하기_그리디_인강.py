'''
[P]
숫자(0~9)로 이루어진 문자열 S가 주어졌을 때 숫자 사이에 '+','*' 연산자를 넣어 만들어질 수 있는 가장 큰 수를 반환
    1. 모든 연산은 왼쪽부터 순서대로 수행
[S]
1. 그리디 알고리즘 _ 0과 1이 아닌 경우에는 '곱하기' 연산이 '더하기'연산 보다 더 값을 키워줌
    정당성 : 0과 1을 제외한 경우 == 2이상부터 곱하기가 더하기보다 큰 수를 만들어 준다. => 특정 경우(0,1)를 처리하여 최적의 해 성립
[L]
1. 함수 이용
    PARAM : nums(list)
    LOGIC : val = val+n if n in except_num else val*n
    RETURN : val
'''


def gready(nums):
    except_num = {0, 1}
    val = 0

    for n in nums:
        val = val+n if val in except_num else val*n

    return val


s = list(map(int, input()))

ret = gready(s)

print(ret)
