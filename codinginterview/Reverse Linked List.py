# Definition for singly-linked list.
# #풀이1 재귀구조로 뒤집기
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode: #연결리스트 입력
#         def reverse(node: ListNode, prev: ListNode = None):
#             if not node:
#                 return prev
#             next, node.next = node.next, prev #node next에 prev리스트를 게속 연결해주면서 None이 되면 최종적으로 거꾸로 연결됨
#             return reverse(next, node) 

#         return reverse(head) #역순서로 됨

#풀이2 반복구조로 뒤집기
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None 

        while node:
            next, node.next = node.next, prev #다중할당 next를 node에 그거를 prev에
            prev, node = node, next #반복문으로 돌면서 게속 반복

        return prev #끝나면 뒤집혀 있음