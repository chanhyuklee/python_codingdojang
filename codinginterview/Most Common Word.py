import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph) #정규표현식으로 쉼표와 마침표를 공백으로 변환
            .lower().split() #대소문자 구분 안하므로 전부 소문자로 변경
                 if word not in banned] #ban된 단어인지 확인

        counts = collections.Counter(words) #Counter함수로 횟수 체크
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]