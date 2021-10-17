'''
define : 그룹단어 = 각 문자가 연속해서 나오는 경우를 의미
kp
#1. 댄어에 속하는 문자의 count() 값과 find()로 index를 찾은 뒤 문자가 같을 때까지 cnt한 값이 같은지 판별
logic
#0. 그룹 단어 개수를 카운트할 ret 선언
#1. 단어 개수(n)만큼 반복
#2. 단어의 중복 제거된 문자(set)만큼 반복
#3. 단어에서 문자 첫 인덱스(find)로 받고 그 뒤 인덱스가 같은 문자가 아닐때까지 반복(while)하며 cnt
#4. 3에서 구한 cnt 값과 단어의 문자 개수(count())값과 같으면 ret +=1
#5. 결과 반환
'''

# ret = 0
# for _ in range(int(input())):
#     visit = set()
#     stack = []
#     is_group = True
#     for c in input():
#         if c in visit:
#             is_group = False
#             break
#         while stack and stack[-1] != c:
#             visit.add(stack.pop())
#             stack = [c]

#         stack.append(c)

#     if is_group == True:
#         ret += 1

# print(ret)


# a = 0
# for i in range(int(input())):
#     s = input()
#     a+= list(s) == sorted(s,key=s.find)
# print(a)


ret = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        ret += 1
print(ret)
