start, stop = map(int, input().split())
if (1<=start<=1000) and (10<=stop<=1000):
    if start<stop:
        for i in range(start, stop+1):
            if i % 5 == 0 and i % 7 == 0:
                print("FizzBuzz")
            elif i % 5 ==0:
                print("Fizz")
            elif i% 7 == 0:
                print("Buzz")
            else:
                print(i)
    else:
        print("처음 값이 나중 값보다 작아야 됩니다.")
else:
    print("범위 내의 값을 입력하세요.")
