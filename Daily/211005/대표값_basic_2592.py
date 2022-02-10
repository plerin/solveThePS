'''
goal : 평균값과 최빈값을 구하라
0. 라이브러리 추가 _ Counter(최빈값 구하기 위함)
1. 입력 받기
    1) 10줄에 걸쳐 입력 받아서 리스트에 담기
    2) sum()/len() 과 Counter에 담아 most_common()[0]반환

'''
# from collections import Counter

ret = []

for _ in range(10):
    ret.append(int(input()))

# cnt = Counter(ret)

# print(sum(ret)//len(ret), cnt.most_common(1)[0][0],sep='\n')

print(sum(ret)//10, max(set(ret), key=ret.count), sep='\n')
