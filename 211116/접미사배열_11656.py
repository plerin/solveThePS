'''
> P
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬한 배열
문자열 S가 주어졌을 때 접미사 배열출력하라
> S
구현
접근
    1. 단어의 접미사 배열 어떻게 만들어?
        - len(word)만큼 for문 반복하며 splice를 통해 ret에 담아
        - 정렬해 그냥 sorted 해도되고 key=lambda x: x[0] 가능
'''

str = input()
ret = []
for i in range(len(str)):
    ret.append(str[i:])

# ret.sort(key=lambda x: x[0])
ret.sort()
print(*ret, sep='\n')
