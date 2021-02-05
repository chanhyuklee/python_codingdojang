from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]: #리스트입력
        answer = [0] * len(T) #첫번쨰 인덱스 길이 측정
        stack = []
        for i, cur in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > T[stack[-1]]:
                last = stack.pop() #빼내고
                answer[last] = i - last #현재꺼와 꺼낸거의 차이가 정답
            stack.append(i)

        return answer