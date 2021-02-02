from typing import List
#타입 어노테이션 활용

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], [] # 문자와 숫자 구분
        for log in logs:
            if log.split()[1].isdigit(): #숫자 판별
                digits.append(log)
            else:
                letters.append(log)

        # 두 개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 문자 로그 정렬 식별자 제외 정렬 후 식별자 정렬
        return letters + digits  #숫자로그는 입력순서대로 이므로 정렬없이 붙여주면 끝

