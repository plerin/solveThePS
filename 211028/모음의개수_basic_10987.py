'''
간단
1. 리스트 컴프리헨션으로 알파벳마다 in 사용하기
2. filter 사용하기
3. 정규표현식 사용하기
'''

# ret = len([c for c in list(map(str, input()))
#            if c in ('a', 'e', 'i', 'o', 'u')])

ret = len([c for c in list(map(str, input()))
           if c in 'aeiou'])
print(ret)
