#쉽게 풀려면 연결리스트->리스트->파이썬 슬라이싱을 통해 홀짝바꾼후 ->연결리스트변환
# Definition for singly-linked list.
#풀이1 반복 구조로 홀짝 노드 처리
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외 처리
        if head is None:
            return None

        odd = head #홀수
        even = head.next #짝수
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next: 
            odd.next, even.next = odd.next.next, even.next.next #홀짝 두칸씩 이동
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head