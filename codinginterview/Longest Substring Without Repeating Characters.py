class Solution: #투포인터 풀이
    def lengthOfLongestSubstring(self, s: str) -> int: #중복없는 가장 긴 부분 문자열
        used = {} 
        max_length = start = 0
        for index, char in enumerate(s): #인덱스와 문자열 같이 추출
            # 이미 등장했던 문자라면 `start` 위치 갱신
            if char in used and start <= used[char]: #이미 등장했던 문자열이면 위치갱신
                start = used[char] + 1
            else:  # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1) #그렇지 않으면 최대 문자열 갱신

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length