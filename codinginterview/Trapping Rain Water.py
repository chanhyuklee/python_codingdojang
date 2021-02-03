from typing import List

#1번 풀이 투포인터를 이용
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1 #입력값의 길이를 최대로 이동
        left_max, right_max = height[left], height[right] #입력값중 가장 큰값을 기준으로 왼쪽과 오른쪽으로 한칸씩 이동

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left] #물높이인 volume을 차례로 더해줌
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume 

#2번 풀이 스택을 이용 
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         stack = [] #스택을 쌓을 리스트 생성
#         volume = 0 #최초 물의 높이는 0

#         for i in range(len(height)):
#             # 변곡점을 만나는 경우
#             while stack and height[i] > height[stack[-1]]: #높이의 차이가 생길때마다
#                 # 스택에서 꺼낸다
#                 top = stack.pop() #낮아지면

#                 if not len(stack):
#                     break

#                 # 이전과의 차이만큼 물 높이 처리
#                 distance = i - stack[-1] - 1
#                 waters = min(height[i], height[stack[-1]]) - height[top]

#                 volume += distance * waters

#             stack.append(i)
#         return volume