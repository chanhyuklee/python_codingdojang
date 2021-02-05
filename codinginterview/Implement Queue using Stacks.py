#스택 2개사용한 풀이 push와 peek
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x): #요소를 큐 마지막에 삽입
        self.input.append(x)

    def pop(self): #큐 처음에 있는 요소 제거
        self.peek()
        return self.output.pop()

    def peek(self): #큐 처음에 있는 요소 조회
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self): #비어있는지 여부 확인
        return self.input == [] and self.output == []