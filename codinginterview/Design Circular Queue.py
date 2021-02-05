#배열을 이용해 풀이
class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k 
        self.maxlen = k #k = 큐의 최대길이
        self.p1 = 0 #포인터1
        self.p2 = 0 #포인터2

    # enQueue(): 리어(뒤쪽) 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None: 
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen 
            return True
        else: #None이 아니면 공간이 꽉찬 상태이거나 비정상적인 경우이므로 False
            return False

    # deQueue(): 프론트 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None #p1에 None을 넣어 기존값 삭제
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None