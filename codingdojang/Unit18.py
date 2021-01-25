start, stop = map(int, input().split())

i = start

while True:
    if i % 10 == 3:
        pass
    else:
        print(i, end=' ')
    i += 1
    if stop<i:
        break