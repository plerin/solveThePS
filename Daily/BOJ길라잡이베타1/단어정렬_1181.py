'''
> p
N개의 단어가 들어오면 정렬하시오
    - 길이가 짧은 것부터 -> 사전 순으로
> S
구현 _ sort
1. 리스트에 담는다 _ 만약 해당 문자열이 리스트에 있다면 생략
2. sorted()로 정렬 _ key를 활용해 조건 2개 주기
3. 결과 출력
'''
import sys

input = sys.stdin.readline

N = int(input())
words = list(set([input().rstrip() for _ in range(N)]))

words.sort(key=lambda x: (len(x), x))

print(*words, sep='\n')
