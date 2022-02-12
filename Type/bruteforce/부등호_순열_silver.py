'''
backjoon url -> https://www.acmicpc.net/problem/2529

>> Keyword
완전 탐색, 순열, 조건에 여부 판단하는 메소드 하나 추가!

>> P
두 종류 부등호 '<', '>'가 k개 나열된 순서열 A가 있을 때
부등호를 만족하는 수중 최댓값과 최솟값을 구하라
    - 숫자는 중복되지 않는다(0~9)

>> S
아이디어
주어진 부등호에 숫자를 넣어가며 찾아야해
최댓값과 최솟값 구하려면 정렬을 달리해서 숫자 넣기 -> 최댓값은 내림차순 한 순서열로 로직수행
시작값부터 넣으며 틀리면 돌아와서 그 다음값부터 넣어(백트래킹)
    -> < < > 인 경우 1,2,3 (x) 1,3,2 (0)  2번째 값을 바로 넘어가기

코드
1. 변수 선언
k = int(input())
op = input().split()
num = range(10)

print(solve(0, 0, ''))
num.sort(reverse=True)
print(solve())

def match(num, op, comb):
    if not comb:
        return True

    if op == '<' and num < int(comb[-1]):
        return True
    if op == '>' and num > int(comb[-1]):
        return True
    
    return False

def solve(start, depth, comb) -> int:
    if depth == k:
        return comb
        return
    
    for i in range(start, 10):
        if str(num[i]) not in comb and match(i, op[depth], comb):
            solve(i, depth+1, comb+str(num[i]))

'''


n = int(input())
op = input().split()
c = [False] * 10  # 0~9까지 중복 체크
mx, mn = '', ''  # 최대/최소 값 저장

# 이전 값과 현재값의 연산이 맞는지 판단


def possible(now, prev, op):
    if op == '<':
        return prev < now
    elif op == '>':
        return prev > now
    return True


def solve(depth, comb):
    global mn, mx
    # 종료조건 -> 최소 값이 채워지면 (not len(mn)) 최대 값을 갱신
    if depth == n + 1:
        if not len(mn):
            mn = comb
        else:
            mx = comb
        return

    for i in range(10):
        if not c[i]:
            if depth == 0 or possible(i, int(comb[-1]), op[depth-1]):
                c[i] = True
                solve(depth+1, comb+str(i))
                c[i] = False


solve(0, '')
print(mx)
print(mn)
