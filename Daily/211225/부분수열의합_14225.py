'''
>> P
수열 S가 주어졌을 때 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하라
>> S
나올 수 있는 경우를 모두 구하고 1부터 진행하며 비어 있는 값 반환 후 종료

1.현재 인덱스 값을 포함 x / 포함 o 하는 방향으로 풀어가자

def dfs(idx: int, sum: int):
    - vari : sum(int) _ seq[idx] 값을 더하며 진행, global ans(set)
    - logic
        1) if idx >= N -> return
        2) sum += seq[idx] & ans.add(sum)
        3) dfs(idx+1, sum-seq[idx]) & dfs(idx+1, sum)
'''


def dfs(idx: int, total: int):
    global part

    if idx >= N:
        return

    part.add(total + seq[idx])

    dfs(idx+1, total + seq[idx])
    dfs(idx+1, total)


N = int(input())
seq = list(map(int, input().split()))
part = set()

dfs(0, 0)

part = sorted(list(part), reverse=True)
cnt = 1
ans = 0

while part:
    if cnt != part.pop():
        ans = cnt
        break
    cnt += 1

print(ans if ans != 0 else cnt)
# print(ans) if ans != 0 else print(cnt)
