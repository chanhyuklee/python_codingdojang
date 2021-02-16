import collections


# Definition for singly-linked list.
class ListNode: #키와 값을 보관할 연결리스트
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode) #자료형 선언 => 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성해줌

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size #size의 갯수만큼 모듈로 연산을하고 나머지를 해시값으로 설정
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None: #인덱스에 값이 없다면
            self.table[index] = ListNode(key, value) #인덱스에 key value를 삽입하고 리턴
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index] #해당 리스트에 노드가 존재하는 경우 "해시충돌"
        while p: #인덱스의 첫번쨰 값
            if p.key == key: 
                p.value = value #이미 키가 존재해서 업데이트하고 빠져나오는 경우
                return
            if p.next is None: # 아무것도 하지 않고 빠져나오는 경우
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size #size의 갯수만큼 모듈로 연산을하고 나머지를 해시값으로 설정
        if self.table[index].value is None: #존재하지 않으면 -1 리턴
            return -1

        # 노드가 존재할때 일치하는 키 탐색
        p = self.table[index]
        while p: #인덱스의 첫번쨰 값
            if p.key == key: #해시값이 일치하면
                return p.value #리턴
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size #size의 갯수만큼 모듈로 연산을하고 나머지를 해시값으로 설정
        if self.table[index].value is None: #키가 없다면 그냥 리턴
            return

        # 인덱스의 첫 번째 노드일때 삭제 처리
        p = self.table[index]
        if p.key == key: #키가 일치하면
            self.table[index] = ListNode() if p.next is None else p.next 
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next #현재 노드를 다음 노드로 연결
                return
            prev, p = p, p.next