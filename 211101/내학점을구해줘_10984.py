'''
[P]
T학기에 대한 수강 과목(N)과 각 과목 별 학점(C)와 성적(G)가 주어졌을 때 총 학점과 평점을 출력한다
[S]
유형 : 구현(implementation)
[L]
GPA 구하는 공식을 알아야 해
credit : 학점 // grade : 성적
for i in range(과목):
    credit, grade = a,b
    total_credit += credit
    total_grade += credit*grade

total_grade = total_grade / total_creditT
'''
for _ in range(int(input())):
    total_credit = 0
    total_grade = 0

    for i in range(int(input())):
        credit, grade = map(float, input().split())
        total_credit += credit
        total_grade += credit * grade

    total_grade = total_grade / total_credit

    print(int(total_credit), '{0:.1f}'.format(total_grade))
