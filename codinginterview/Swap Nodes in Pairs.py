# # Definition for singly-linked list.
# # 풀이1 값만 교환 (노드는 유지한체 값만 변경)
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode: #연결리스트 입력
#         cur = head

#         while cur and cur.next:
#             # 값만 교환
#             cur.val, cur.next.val = cur.next.val, cur.val
#             cur = cur.next.next

#         return head


# # Definition for singly-linked list.
# # 풀이2 반복구조로 스왑
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         root = prev = ListNode(None)
#         prev.next = head
#         while head and head.next:
#             # b가 a(head)를 가리키도록
#             b = head.next
#             head.next = b.next
#             b.next = head

#             # prev가 b를 가리키도록
#             prev.next = b

#             # 다음 번 비교를 위해 이동
#             head = head.next
#             prev = prev.next.next
#         return root.next

# 풀이3 재귀 구조로 스왑
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next #포인터 역활
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next) #포인터를 이용하여 바로 리턴
            p.next = head
            return p
        return head