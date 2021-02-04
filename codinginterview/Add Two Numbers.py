# from typing import List

#풀이 1 자료형변환 리스트-> 문자열->숫자->리스트
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     # 연결 리스트 뒤집기
#     def reverseList(self, head: ListNode) -> ListNode: #연결리스트 입력
#         node, prev = head, None

#         while node:
#             next, node.next = node.next, prev #연결리스트 뒤집기
#             prev, node = node, next

#         return prev

#     # 연결 리스트를 파이썬 리스트로 변환
#     def toList(self, node: ListNode) -> List:
#         list: List = []
#         while node:
#             list.append(node.val) #리스트로 변환
#             node = node.next
#         return list

#     # 파이썬 리스트를 연결 리스트로 변환
#     def toReversedLinkedList(self, result: str) -> ListNode:
#         prev: ListNode = None
#         for r in result:
#             node = ListNode(r)
#             node.next = prev
#             prev = node

#         return node

#     # 두 연결 리스트의 덧셈
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         a = self.toList(self.reverseList(l1))
#         b = self.toList(self.reverseList(l2))

#         resultStr = int(''.join(str(e) for e in a)) + \
#                     int(''.join(str(e) for e in b)) #문자열을 인트로 바꿔서 더해줌

#         # 최종 계산 결과 연결 리스트 변환
#         return self.toReversedLinkedList(str(resultStr)) #다시 연결리스트로 변환


# Definition for singly-linked list.
#풀이2 전가산기 구현
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10) #두입력값의 연산을 수행하고 자릿수가 넘어가면 자리올림수를 설정(10진법) divmod는 몫과 나머지로 구성된 튜플을 리턴
            head.next = ListNode(val) #다음자리 수행
            head = head.next

        return root.next