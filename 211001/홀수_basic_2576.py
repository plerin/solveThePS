'''
1. 입력 받기 _ 100이하 자연수 7개
2. 결과 출력 _ sum , min
'''
# 1
odd_list = list(filter(lambda x: x % 2 == 1, [int(input()) for _ in range(7)]))
# 2
if len(odd_list) == 0:
    print(-1)
else:
    print(sum(odd_list), min(odd_list), sep='\n')
