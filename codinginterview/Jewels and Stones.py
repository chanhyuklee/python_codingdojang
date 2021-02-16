# #1번풀이 해시테이블 이용
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         freqs = {} #해시 테이블 선언
#         count = 0

#         # 돌(S)의 빈도 수 계산
#         for char in S: #돌의 빈도수 많큼 숫자 부여
#             if char not in freqs:
#                 freqs[char] = 1
#             else:
#                 freqs[char] += 1

#         # 보석(J)의 빈도 수 합산 
#         for char in J: #보석의 빈도수 많큼 숫자 부여
#             if char in freqs:
#                 count += freqs[char]

#         return count #숫자 리턴(보석의 갯수 리턴)

# #2번풀이 default를 이용한 비교생략

# import collections


# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         freqs = collections.defaultdict(int) #default를 활용하여 존재하지 않는 키는 디폴트를 리턴
#         count = 0

#         # 비교 없이 돌(S) 빈도 수 계산
#         for char in S:
#             freqs[char] += 1

#         # 비교 없이 보석(J) 빈도 수 합산
#         for char in J:
#             count += freqs[char]

#         return count #키가 존재하는지 않하는지 여부를 판단할 필요가 없기떄문에 바로계산 가능

# #3번풀이 counter로 계산생략

# import collections


# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산 #counter을 활용하여 빈도수를 바로 계산
#         count = 0

#         # 비교 없이 보석(J) 빈도 수 합산
#         for char in J:
#             count += freqs[char]

#         return count #빈도수만 세기떄문에 빠름 (존재여부 판단할 필요가 없음)

#4번풀이 파이썬 리스트 컴프리헨션 이용
  
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S) #돌안에 보석이 있는지 반복문으로 돌리고 바로 합산하여 보석갯수 확인 (True False 반환)