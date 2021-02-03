from typing import List
  
# #1번 풀이 리스트의 모든 요소를 일일이 비교
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)): #i를 nums까지
#             for j in range(i + 1, len(nums)): #j를 nums까지
#                 if nums[i] + nums[j] == target: #i와 j가 target일때 반환
#                     return [i, j]

# #2번 풀이 in을 이용한 탐색
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n in enumerate(nums): #인덱스와 i를 차례대로 뽑고
#             complement = target - n #target에서 값을 빼서 변수만듬

#             if complement in nums[i + 1:]:
#                 return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

# #3번 풀이 첫번쨰 수를 타겟에서 뺀뒤 그 값을 탐색
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_map = {}
#         # 키와 값을 바꿔서 딕셔너리로 저장
#         for i, num in enumerate(nums):
#             nums_map[num] = i 

#         # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
#         for i, num in enumerate(nums):
#             if target - num in nums_map and i != nums_map[target - num]:
#                 return [i, nums_map[target - num]]

#4번 풀이 이중 for문을 하나의 for로 통합
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 `for`문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i