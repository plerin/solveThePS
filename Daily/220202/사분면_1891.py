'''
>> P
좌표평면에 4개 사분면으로 나뉜다.
각 사분면을 다시 사분면으로 나누어 번호를 붙인다.

>> S
접근
1. 좌표를 찾는다
    - 재귀를 통해 1/2/3/4분면을 구분
2. 좌표를 이동한다
    - 해당 좌표가 범위 안에 있으면 구하는 재귀 로직 수행 아니면 -1 출력
'''

d, num = input().split()
d = int(d)
x, y = map(int, input().split())


def find_coordinate(num, idx, r, c, size):
    if size == 0:
        global num_r, num_c
        num_r, num_c = r, c
        return

    if num[idx] == '1':
        find_coordinate(num, idx+1, r, c+size, size//2)
    elif num[idx] == '2':
        find_coordinate(num, idx+1, r, c, size//2)
    elif num[idx] == '3':
        find_coordinate(num, idx+1, r+size, c, size//2)
    elif num[idx] == '4':
        find_coordinate(num, idx+1, r+size, c+size, size//2)


def make_answer(num_r, num_c, size, ans):
    if size == 0:   # base_condition을 size로 기준잡음
        print(ans)
        return

    # size는 (2**d)에서 //2 된 값이기 때문에 size를 기준으로 사분면을 나눠
    # 1사분면 이면 col이 size만큼 더 나아간거니까 num_c - size 빼고 size//2 , ans + '1' 한 뒤 재귀 호출
    if 0 <= num_r < size and size <= num_c < 2*size:
        make_answer(num_r, num_c-size, size//2, ans+'1')
    elif 0 <= num_r < size and 0 <= num_c < size:
        make_answer(num_r, num_c, size//2, ans+'2')
    elif size <= num_r < 2*size and 0 <= num_c < size:
        make_answer(num_r-size, num_c, size//2, ans+'3')
    elif size <= num_r < 2*size and size <= num_c < 2*size:
        make_answer(num_r - size, num_c - size, size//2, ans+'4')


num_r = num_c = 0
# 좌표 찾고
find_coordinate(num, 0, num_r, num_c, (2**d)//2)

# 좌표 이동
num_r -= y  # 위쪽 == 양수 / 아래쪽 == 음수 ,, 보통 아래쪽이 양수인데 이경우는 반대니까 빼준다
num_c += x  # 오른쪽 == 양수 / 왼쪽 == 음수

# 해당 좌표 -> 사분면 번호 구하기
if 0 <= num_r < 2**d and 0 <= num_c < 2**d:
    make_answer(num_r, num_c, (2**d)//2, '')
else:
    print(-1)
