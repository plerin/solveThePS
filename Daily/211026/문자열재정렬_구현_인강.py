'''
[P]
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 주어졌을 때 정렬된 값을 출력
    - 알파벳 : 오름차순정렬, 앞
    - 숫자 : 모두 더한 합, 뒤
[S]
구현(inplementation) _ 문자열 재정렬

[L]
1. 변수 선언
    - S(list) _ 입력 값 _ 대문자 알파벳과 숫자가 합쳐진 문자열를 입력 값으로 받음
    - str(list) _ 알파벳담는 리스트
    - num(int) _ 숫자 만날 때마다 갱신
2. 로직
    1) loop with S
    2) if isdigit() then str.append(a) else then num+=a
3. 결과 출력
'''

S = list(map(str, input()))
ret, num = [], 0

for a in sorted(S):
    if a.isdigit():
        num += int(a)
    else:
        ret.append(a)

if num != 0:
    ret.append(str(num))

print(''.join(ret))
