class Solution:
    def isValid(self, s: str) -> bool: 
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table: #테이블에 있으면
                stack.append(char) #스택에 넣음
            elif not stack or table[char] != stack.pop(): #예외처리 스택이 비어있는 여부 체크
                return False
        return len(stack) == 0