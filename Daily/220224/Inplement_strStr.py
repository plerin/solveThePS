'''
>> P 
haystack안에 needle 첫번째 인덱스 반환 
    - needle이 haystack에 없다면 -1 
    - needle이 0이면 0 리턴
>> S
3가지 경우
1. if needle == '' then return 0
2. 아니면 find로 찾기

시간복잡도 : O(n)
공간복잡도 : O(1)
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        return haystack.find(needle)
