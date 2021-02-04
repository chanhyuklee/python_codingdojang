# Definition for singly-linked list.
class ListNode: #연결리스트
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: #연결리스트 2개 입력받음
        if (not l1) or (l2 and l1.val > l2.val): #l1이 l2보다 크면 변경 (작은값이 왼쪽으로 오도록)
            l1, l2 = l2, l1 
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2) #l1이 작으면 l1한번더
        return l1 #병합되면서 l1으로 통합