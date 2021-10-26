'''
[P]
W 대학, K 대학 각각 10명의 점수르 입력 받아 득점이 높은 사람 3명의 점수를 합산하여 출력

[S]
구현(implementation) _ 개행을 구분자로 한 입력 값 중 큰 3개의 값을 합한 값 출력

[L]
1. 20개를 모두 하나의 리스트에 입력 받기 
2. 슬라이싱으로 [:10], [10:]나누며 정렬(내림차순)
3. [:3]_ 앞 3개까지 슬라이싱하여 sum() 구해 출력
'''

scores = [int(input()) for _ in range(20)]

w_coll = sum(sorted(scores[:10], reverse=True)[:3])
k_coll = sum(sorted(scores[10:], reverse=True)[:3])

print(w_coll, k_coll)
