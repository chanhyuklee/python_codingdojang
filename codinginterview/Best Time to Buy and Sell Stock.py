import sys
from typing import List

# #풀이1 전 구간 탐색
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_price = 0

#         for i, price in enumerate(prices):  
#             for j in range(i, len(prices)):
#                 max_price = max(prices[j] - price, max_price) #최대는  최대에서 최소 뺸것

#         return max_price


#풀이2 저점과 현재 값과의 차이 계산
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize 

        # 최소값과 최대값 계속 갱신
        for price in prices:
            min_price = min(min_price, price) #최소값을 미리 구해놓음
            profit = max(profit, price - min_price) #price가 하나씩 증가하면서 가장 큰값을 최대이익으로 저장

        return profit