import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque() #데크로 변환

    def push(self, x): #스택에 요소 삽입
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self): #스택의 첫 요소 삭제
        return self.q.popleft()

    def top(self): #스택의 첫 요소 가져옴
        return self.q[0]

    def empty(self): #스택 비어있는지 여부 리턴
        return len(self.q) == 0