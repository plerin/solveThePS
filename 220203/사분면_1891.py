'''
>> P
좌표평면 위 사분면으로 나뉠 때
하나의 사분면 조각을 이동시켰을 때 그 조각이 도착한 사분면 번호를 알아내라
    - x : 오른쪽 이동 = 양수, 왼쪽 이동 = 음수
    - y : 위쪽이동 = 양수, 아래 이동 = 음수(우리가 사용하는 방식이랑 반대)
>> S
1. 사분면이 주어지고
2. 이동하고
3. 해당 사분면을 구하라

접근
1. 사분면의 좌표를 얻고
2. 이동하고
3. 해당 좌표의 사분면 정보를 얻는다.

사분면의 사분면을 구한다 = 재귀
사분면 자릿수가 n이면 한 변의 최대 길이는 2**n
    -> n = 3, 최대 길이 8

코드
0. 입력 받기
import sys
input = sys...

d, num = input().split()
x, y = map(int, input().split())

1. 사분면을 통해 좌표 구하는 함수(재귀)
def get_coordinate(num, idx, x, y, size):
    if size == 0:
        global num_r, num_c
        num_r, num_c = x, y
        return
    
    if num[idx] == '1':
        get_coordinate(num, idx+1, x, y+size, size//2)
    elif num[idx] == '2':
        get_coordinate(num, idx+1, x, y, size//2)
    elif num[idx] == '3':
        get_coordinate(num, idx+1, x+size, y, size//2)
    elif num[idx] == '4':
        get_coordinate(num, idx+1, x+size, y+size, size//2)

2. 좌표 이동
num_r += x
num_c -= y

3. 좌표가 존재여부 판단
if 0 <= num_r < 2**d and 0 <= num_c < 2**d:
    사분면 확인 함수 호출
else:
    print(-1)

4. 좌표를 통해 사분면 구하는 함수(재귀) 
def get_answer(num_r, num_c, size, ans):
    if size == 0:
        print(ans)
        return
    
    if 0 <= num_r < size and size <= num_c < 2*size:
        get_answer(num_r, num_c-size, size//2, ans+'1')
    elif 0 <= num_r < size and 0 <= num_c < size:
        get_answer(num_r, num_c, size//2, ans+'2')
    elif size <= num_r < 2*size and 0 <= num_c < size:
        get_answer(num_r-size, num_c, size//2, ans+'3')
    elif size <= num_r < 2*size and size <= num_c < 2*size:
        get_answer(num_r-size, num_c-size, size//2, ans+'4')
'''

# d는 int로 num은 str으로 사용할 것
d, num = input().split()
d = int(d)
x, y = map(int, input().split())

# param : 사분면, index, x, y, size


def get_coordinate(num, idx, x, y, size):
    if size == 0:
        global num_r, num_c
        num_r, num_c = x, y
        return

    # 어떤 사분면인지에 따라 x, y 좌표 이동해줘 _ 각 분면의 특징 활용
    if num[idx] == '1':
        get_coordinate(num, idx+1, x, y+size, size//2)
    elif num[idx] == '2':
        get_coordinate(num, idx+1, x, y, size//2)
    elif num[idx] == '3':
        get_coordinate(num, idx+1, x+size, y, size//2)
    elif num[idx] == '4':
        get_coordinate(num, idx+1, x+size, y+size, size//2)


def get_answer(num_r, num_c, size, ans):
    if size == 0:
        print(ans)
        return

    # 한 면은 사분면 갯수(n)에 따라 2**n 으로 커지기 때문에 size//2 한 값이 중간을 의미
    # 이를 통해 어떤 분면에 속해있는지 확인하고 r(row), c(col) 값을 이동
    if 0 <= num_r < size and size <= num_c < 2*size:
        get_answer(num_r, num_c-size, size//2, ans+'1')
    elif 0 <= num_r < size and 0 <= num_c < size:
        get_answer(num_r, num_c, size//2, ans+'2')
    elif size <= num_r < 2*size and 0 <= num_c < size:
        get_answer(num_r-size, num_c, size//2, ans+'3')
    elif size <= num_r < 2*size and size <= num_c < 2*size:
        get_answer(num_r-size, num_c-size, size//2, ans+'4')


num_r = num_c = 0
get_coordinate(num, 0, num_r, num_c, (2**d)//2)
num_r -= y
num_c += x

if 0 <= num_r < 2**d and 0 <= num_c < 2**d:
    get_answer(num_r, num_c, (2**d)//2, '')
else:
    print(-1)
