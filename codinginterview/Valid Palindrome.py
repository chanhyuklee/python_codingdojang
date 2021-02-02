#방법 1
class Solution:
    def isPalindrome(self, s: str) -> bool: 
        strs = []
        for char in s:
            if char.isalnum(): #알파벳 숫자일때만 리스트에 추가
                strs.append(char.lower())  #소문자로 변경

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

# #방법 2 - 더 빠름
# import re  #정규표현식 사용하기 위해 임포트

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         #정규식으로 불필요한 문자 필터링
#         s = re.sub('[^a-z0-9]', '', s)
                
#         return s == s[::-1] #슬라이싱
            
