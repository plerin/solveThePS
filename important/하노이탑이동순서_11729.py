'''
>> P
3개 장대가 있고 N개의 원판이 있을 때 규칙에 따라 1번 장대에서 3번 장대로 최소 횟수로 옮겨야한다
수행과정을 출력하라
    - 조건
        1) 한 번에 한 개의 원판만 옮길 수 있다.
        2) 원판은 항상 위의 것이 아래 것보다 작아야 한다.
>> S
이름만 들어도 어렵게 느껴지는 하노이 탑 제가 한 번 극복해보겠습니다

1 -> 3으로 N개를 옮겨야 할 때

1. 1 -> 2으로 N-1개를 옮김
2. 1 -> 3으로 1개를 옮김
3. 2 -> 3으로 N-1개를 옮김

접근
DFS를 이용한 풀이 
dfs(from, to, tmp, num)
dfs(1, 2, 3, N-1)
dfs(1, 3, 2, 1)
dfs(2, 3, 1, N-1)


N = 5, 1- > 3
4개 1 -> 2 // 1개 1 -> 3 // 4개 2 -> 
N = 4, 1- > 2
3, 1 -> 3 // 1, 1 -> 2 // 3 3 -> 1
N = 3, 1- > 3
2, 1 -> 2 // 1, 1 -> 3 // 2, 2-> 3
N = 2, 1- > 2
1, 1 -> 3 // 1, 1 -> 2 // 1, 3 -> 2

규칙 찾았잖아 코딩 그대로 하면 됐어!!

n개를 1 -> 3으로 옮길 때
n-1개를 1 -> 2로 
1개를 1 -> 3으로 
n-1개를 2 -> 3으로 !!

코딩으로...
def hanoi(fm, to, tmp, num):
    if num == 1:    # 기저 조건
        print(fm, to)
    else:
        print(fm, tmp, to, num-1)
        print(fm, to)
        hanoi(tmp, to, fm, num-1)

개수 구하는 방법
n == 1일때 -> 1가지
n == 2일때 -> 1개 이동 , 1개 이동, 1개 이동 == 3가지
n == 3 -> 2개 이동, 1개 이동, 2개 이동 == n==2일때 *2 + 1
n == 4 -> 3개 이동, 1개이동 , 3개 이동 -> n==3일 때 * 2 + 1

cnt = 1
for i in range(n-1):
    cnt = cnt * 2 + 1

'''
# n = int(input())

# def hanoi(fm, to, tmp, num):
#     global cnt
#     cnt += 1

#     if num == 1:
#         print(fm, to)
#     else:
#         hanoi(fm, tmp, to, num-1)
#         print(fm, to)
#         hanoi(tmp, to, fm, num-1)


# cnt = 1
# for i in range(n-1):
#     cnt = cnt * 2 + 1
# print(cnt)
# hanoi(1, 3, 2, n)

def hanoi2(n: int, start: int, end: int) -> None:
    if n == 1:  # 기저 조건 n == 1일 때
        print(start, end)
        return

    hanoi2(n-1, start, 6-start-end)  # 6-start-end 는 start, end가 아닌 나머지 기둥을 의미!
    print(start, end)
    hanoi2(n-1, 6-start-end, end)


n = int(input())
print(n**2-1)   # 하노이 탑 이동 횟수 => d(n) = d(n-1) * 2 + 1
hanoi2(n, 1, 3)
