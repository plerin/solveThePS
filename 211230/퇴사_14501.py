'''
>> P
N+1일에 퇴사를 하려고 할 때 얻을 수 있는 최대 이익을 구하라
    - Ti를 상담했을 때 Pi를 얻을 수 있다.
    - 남을 일수와 일자별 소요 일과 획득 보수가 주어진다.
>> S
해당 일자를 수락했을 때 일어날 수 있는 모든 경우의 수를 구하기

def dfs(day: int, earning: int):
    - param : day - 일자, earing - 누적 보수
    - vari : table(list) - (day, earning), global ans(int) _ max 저장
    - logic
        1) if day > N -> update ans & return
        2) for i in range(N)
            -> day, earn = table[i] -> if now + day <= N -> dfs(now+day, earning_earn) else 
        3) 
'''


def dfs(now: int, total: int):
    global ans

    if now >= N:
        ans = max(ans, total)
        return

    for i in range(now, N):
        day, earn = table[i]

        if i + day <= N:    # 누적 일자에서 소요 일자를 더했을 때 작으면
            dfs(i+day, total+earn)
        else:
            dfs(i+day, total)


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dfs(0, 0)

print(ans)
