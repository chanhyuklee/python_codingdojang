from typing import List

# #풀이 1 일일이 다 탐색
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = [] #리스트 생성
#         nums.sort() #정렬

#         # 브루트 포스 n^3 반복
#         for i in range(len(nums) - 2):
#             # 중복된 값 건너뛰기
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             for j in range(i + 1, len(nums) - 1):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue
#                 for k in range(j + 1, len(nums)):
#                     if k > j + 1 and nums[k] == nums[k - 1]:
#                         continue
#                     if nums[i] + nums[j] + nums[k] == 0:  #반복문 돌면서 3수의 합이 0일떄 리스트에 추가
#                         results.append([nums[i], nums[j], nums[k]])

#         return results

#풀이 2 투포인터 이용
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = [] #리스트 생성
        nums.sort() #정렬

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 `sum` 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:   #0보다 작으면 왼쪽으로 이동
                    left += 1
                elif sum > 0: #0보다 크면 오른쪽으로 이동
                    right -= 1
                else: 
                    # `sum = 0`인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results