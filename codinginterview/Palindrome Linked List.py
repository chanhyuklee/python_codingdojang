#풀이1 리스트로 변환 후 펠린드롬판별
# from typing import List

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         q: List = [] #리스트생성

#         if not head:
#             return True

#         node = head
#         # 리스트 변환
#         while node is not None: #반복문으로 끝까지 이동
#             q.append(node.val)
#             node = node.next #오른쪽으로 한칸씩 이동

#         # 팰린드롬 판별
#         while len(q) > 1:
#             if q.pop(0) != q.pop(): #한개씩 뽑아서 펠린드롬 판별
#                 return False

#         return True

#풀이2 테크를 이용하여 최적화 
# import collections
# from typing import Deque


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         # 데크 자료형 선언
#         q: Deque = collections.deque()

#         if not head:
#             return True

#         node = head
#         while node is not None:
#             q.append(node.val)
#             node = node.next

#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False

#         return True




#풀이3 런너를 이용하여 풀이
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head #slow, fase 두개의 포인터 설정
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next #fast는 2칸씩 이동
            rev, rev.next, slow = slow, rev, slow.next  #fast가 끝나면 slow는 정확히 중간에 위치 (다중할당)
        if fast:
            slow = slow.next #slow는 1칸씩 이동

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val: #slow가 중간위치이므로 rev를 slow와 비교하면서 판별
            slow, rev = slow.next, rev.next
        return not rev