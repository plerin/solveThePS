'''
>> P
수열 S가 주어졌을 때 부분 수열의 합으로 나올 수 없는 거장 작은 자연수 구하기
>> S
1. 부분수열의 합을 구하기
    - combination 활용
    - 모든 경우의 수 만들기(부루트포스-재귀)
    def dfs(depth:int, total: int):
        if depth == 3:
            return
        part_sum.add(total)
        for i in range(N):
            if visited[i]: continue
            visited[i] = True & dfs(depth+1, total+seq[i]) & visited[i] = False
2. 가장 작은 자연수 구하기
    - 정렬 후 반복문으로 i와 val이 같지 않으면 출력 그런 경우가 없으면 i 다음 값 출력
    arr =[i for i in range(len(part_sum)) if (i+1) != part_sum[i]] 
    print(arr[0]) if len(arr) != 0 else print(0)
        
'''


def dfs(start: int, total: int):
    global part

    part.add(total)

    for i in range(start, N):
        if visited[i]:
            continue

        visited[i] = True
        dfs(i, total+seq[i])
        visited[i] = False


N = int(input())
seq = list(map(int, input().split()))
visited = [False] * N
part = set()

dfs(0, 0)
part = list(part)
part.sort()

ans = [i for i in range(len(part)) if i != part[i]]

print(ans[0]) if len(ans) != 0 else print(part[-1]+1)
