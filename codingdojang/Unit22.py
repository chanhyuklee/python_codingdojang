a = []
num1, num2 = map(int, input().split())
if 1<=num1<=20 and 10<=num2<=30:
    if num1<num2:
        for i in range(num1, num2+1):
            a.extend([2**i])
    else:
        print('첫번쨰 값이 두번째 값보다 작아야됩니다.')
else:
    print('입력값 범위 오류')
a.pop(len(a)-2)
a.pop(1)
print(a)