'''
>> P
ATM 앞에 N명이 기다리고 있고 i번 사람이 돈을 일출하는데 걸리는 시간은 Pi이다
기다리는 순서에 따라 앞사람 소요시간이 추가될 때 모든 사람이 인출하는데 걸리는 최소 소요값을 구하라
>> S
그리디 알고리즘 문제는 조건을 활용해 가장 효율적인 로직을 찾고 그대로 값을 구한다.
N명의 사람의 순서를 정렬해서 최소 값을 구하면 됨
소요시간이 짧은 사람이 먼저 해야 짧은 대기시간이 짧아짐
    -> 오름차순 정렬 후 누적 값 구하기

def solve():
    global time # 오름차순 정렬 후
    ret = 0
    for i in range(len(time)):
        ret += sum(time[:i+1])
'''


def solve():
    global time

    ret = 0
    for i in range(len(time)):
        ret += sum(time[:(i+1)])
    print([time[:(i+1)] for i in range(len(time))])
    return ret


N = int(input())
time = sorted(list(map(int, input().split())))

ans = solve()

print(ans)
