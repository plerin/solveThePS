''''
[P]
소/대문자로 이루어진 문자열을 입력 받아 대문자->소문자, 소문자->대문자로 바꿔 출력
[S]
구현문제 _ 파이썬 기본 라이브러리
[L]
1. 입력 받음
    - s(str) : 문자열
2. map(lambda x: x.upper() if x.islower() else x.lower())
3. 문자열로 변환하여 출력(''.join()
'''

s = map(str, input())
ret = map(lambda x: x.upper() if x.islower() else x.lower(), s)
print(''.join(ret))
