'''
> P
영어 소문자만 기록할 수 있는 한 줄 에디터를 만드려고한다.
명령어는 4개로 이뤄져있으며 모든 명령어를 수행한 뒤 입력된 문자열을 구하는 프로그램을 작성하시오
    - 커서는 맨 뒤에 위치
> S
범위 : N - 0~ 10만 // M - 1~50만 => sys 사용하기
유형 : 구현
1. 입력 문자열을 문자열 리스트로 변환 후 연산해보자
    - l (idx-1 if idx != 0) // D (idx+1 if idx != len(arr)-1) // B([:idx]+[idx:]) , idx 유지 // P :  insert(idx,'문자')
'''
import sys

input = sys.stdin.readline

s = list(map(str, input()))
idx = len(s)-1

for _ in range(int(input())):
    cmd = input()

    if cmd.startswith("L"):
        idx = idx-1 if idx != 0 else idx
    elif cmd.startswith("D"):
        idx = idx+1 if idx != len(s)-1 else idx
    elif cmd.startswith("B"):
        idx = idx-1 if idx >= 1 else idx
        s = s[:idx]+s[idx+1:]
    elif cmd.startswith("P"):
        s.insert(idx, cmd.split()[1])
        idx += 1

print(''.join(s))
