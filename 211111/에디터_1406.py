'''
> 영어 소문자만 기록할 수 있는 에디터 만들자
    - 기능은 총 4개
    - 커서 위치 가능한 곳 3개(첫 문자 왼쪽 / 가운데 / 마지막 문자 오른쪽) ex) .a.b.

'''
import sys

input = sys.stdin.readline

st1 = list(map(str, input().rstrip()))
st2 = []

for _ in range(int(input())):
    cmd = input()

    if cmd[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif cmd[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif cmd[0] == 'B':
        if st1:
            st1.pop()
    elif cmd[0] == 'P':
        st1.append(cmd[2])
print(''.join(st1 + list(reversed(st2))))
# print(''.join(st1.append(reversed(st2))))
