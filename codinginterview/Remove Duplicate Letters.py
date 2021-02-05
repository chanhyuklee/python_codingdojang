# #풀이1 재귀를 이용한 제거
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         # 집합으로 정렬
#         for char in sorted(set(s)):
#             suffix = s[s.index(char):]
#             # 전체 집합과 접미사 집합이 일치할때 분리 진행
#             if set(s) == set(suffix):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ''))
#         return ''

import collections

#풀이2 스택을 이용한 제거
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), [] #카운터, 집합, 리스트

        for char in s:
            counter[char] -= 1
            if char in seen: #이미 처리된 문자는 건너뜀
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0: #카운터가 0이상이면 앞에 문자 제거 (뒤에서 다시 붙일 수 있기 떄문에)
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)