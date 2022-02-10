'''
1. 각 자리의 숫자를 더한다
2. 주어진 수의 오른쪽 자리와 1번의 오른쪽 자리수를 이어붙인다
1,2번 반복해서 원래 수로 돌아오는데 걸리는 횟수 반환

'''
# N = input()
# if len(N) == 1:
#     N = '0'+N
# n1 = N
# cnt = 0

# while True:
#     cnt += 1
#     n2 = str(sum(map(int, n1)))
#     n3 = n1[-1]+n2[-1]
#     if n3 == N:
#         break
#     else:
#         n1 = n3

# print(cnt)


'''
n을 입력받는다고 했을 때
n의 일의자리 + (n의 십의자리 + 일의자리)의 일의자리가 n과 같을 때까지
'''

N = int(input())
cnt = 0
cn = N
while cn != N or cnt == 0:
    cn = (cn % 10)*10 + (cn//10+cn % 10) % 10
    cnt += 1

print(cnt)
