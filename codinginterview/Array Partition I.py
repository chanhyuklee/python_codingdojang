from typing import List

# #풀이 1 오름차순으로 정렬 후 2개씩 짝
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         pair = []
#         nums.sort()

#         for n in nums:
#             # 앞에서 부터 오름차순으로 페어를 만들어 합 계산
#             pair.append(n)
#             if len(pair) == 2:
#                 sum += min(pair)
#                 pair = []

#         return sum

        
# #풀이 2 오름차순 정렬 후 짝수번째만 계산 (짝수가 항상 작은값이기 떄문)
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         nums.sort()

#         for i, n in enumerate(nums):
#             # 짝수 번째 값의 합 계산
#             if i % 2 == 0:
#                 sum += n

#         return sum

#풀이3 파이썬 슬라이싱 활용 정렬 후 2칸씩 이동
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])