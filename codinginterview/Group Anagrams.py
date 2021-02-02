import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) #에러가 발생하지 않도록 default 값 설정

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word) #join(sorted)는 문자열로 반환 그이후 다시 append해서 anagrams을 만듬
        return list(anagrams.values()) #만들어진 anagrams의 값들을 리스트로 반환