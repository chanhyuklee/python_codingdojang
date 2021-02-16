import collections
import heapq
from typing import List


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freqs = collections.Counter(nums)
#         freqs_heap = []  #우선순위 큐 사용
#         # 힙에 음수로 삽입 
#         for f in freqs:
#             heapq.heappush(freqs_heap, (-freqs[f], f)) #파이썬은 최소 힙만 지원 

#         topk = list()
#         # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
#         for _ in range(k): #k번이상인 횟수만 topk리스트에 담는다
#             topk.append(heapq.heappop(freqs_heap)[1])

#         return topk


#2번 풀이 파이썬 most_common활용
import collections


class Solution:
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k)))[0] #counter와 최대 공통갯수 K를 zip으로 묶어서 *로 언패킹 추출 